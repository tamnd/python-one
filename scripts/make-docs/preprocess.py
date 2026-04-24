#!/usr/bin/env python3
"""
Pre-process a Python documentation LaTeX file for pandoc.

What it does:
  - Recursively expands \\input{file} relative to the source directory
  - Converts the old-style backslash-delimited \\verb\\text\\ to \\verb|text|
  - Strips \\documentstyle / \\documentclass headers (replaces with bare article)
  - Strips document structure commands that confuse pandoc
  - Strips index-only commands
  - Strips \\ifhtml...\\fi conditional blocks
  - Preserves the body, from \\begin{document} to \\end{document}

Usage:
  preprocess.py <input.tex> [base_dir]

Writes preprocessed LaTeX to stdout.
"""
import re
import sys
import os

STRIP_CMDS = {
    # zero-arg commands to remove entirely
    r'\maketitle', r'\tableofcontents', r'\makeindex',
    r'\makemodindex', r'\modsubindex',
}

STRIP_ONE_ARG = {
    # single-arg commands whose argument is also discarded
    r'\pagenumbering', r'\pagestyle', r'\thispagestyle',
    r'\setcounter', r'\addtolength', r'\setlength',
    r'\vspace', r'\hspace', r'\vskip', r'\hskip',
    r'\enlargethispage',
}

_expanded: set = set()


def read_file(path: str) -> str:
    for enc in ('utf-8', 'latin-1', 'cp1252'):
        try:
            with open(path, encoding=enc, errors='replace') as f:
                return f.read()
        except Exception:
            pass
    return ''


def expand_inputs(text: str, base_dir: str, depth: int = 0) -> str:
    """Recursively inline \\input{filename} references."""
    if depth > 10:
        return text

    # Files that produce noise (copyright notices, index files) -- skip them
    SKIP_FILES = {'copyright', 'copyright.tex', 'ref.ind', 'ref.ind.tex'}

    def replace_input(m: re.Match) -> str:
        fname = m.group(1).strip()
        if not fname.endswith('.tex'):
            fname += '.tex'
        if os.path.basename(fname) in SKIP_FILES:
            return ''
        full = os.path.join(base_dir, fname)
        if not os.path.exists(full):
            # try just the basename
            full = os.path.join(base_dir, os.path.basename(fname))
        if not os.path.exists(full):
            return f'% [missing input: {fname}]\n'
        sub = read_file(full)
        return expand_inputs(sub, os.path.dirname(full), depth + 1)

    return re.sub(r'\\(?:input|include)\{([^}]+)\}', replace_input, text)


def fix_verb(text: str) -> str:
    r"""
    Convert old-style \verb\text\ (backslash delimiters) to \verb|text|.
    Also handles other single-char delimiters that pandoc may not like.
    Pandoc handles \verb|text| and \verb+text+ natively.
    """
    result = []
    i = 0
    while i < len(text):
        if text[i:i+5] == r'\verb' and i + 5 < len(text) and text[i + 5] != '{':
            delim = text[i + 5]
            i += 6
            end = text.find(delim, i)
            if end == -1:
                result.append(r'\verb')
                result.append(delim)
                continue
            inner = text[i:end]
            # Replace any | inside with a space to avoid pandoc confusion
            safe_inner = inner.replace('|', ' ')
            result.append(r'\verb|' + safe_inner + r'|')
            i = end + 1
        else:
            result.append(text[i])
            i += 1
    return ''.join(result)


def strip_doc_structure(text: str) -> str:
    r"""
    Remove document-level boilerplate.
    Replace \documentstyle/\documentclass with a plain article header.
    Extract the body between \begin{document} and \end{document}.
    """
    # Normalise documentstyle -> documentclass article
    text = re.sub(
        r'\\documentstyle\s*(\[[^\]]*\])?\s*\{[^}]*\}',
        r'\\documentclass{article}',
        text
    )
    # Keep only the body
    body_match = re.search(
        r'\\begin\{document\}(.*?)\\end\{document\}',
        text, re.DOTALL
    )
    if body_match:
        body = body_match.group(1)
    else:
        # No \begin{document} - take everything after preamble-ish lines
        body = re.sub(r'(?s).*?(%.*?\n)?(?=\\(chapter|section|title|abstract))', '', text, count=1)
        if not body:
            body = text

    # Remove maketitle / TOC / page numbering
    body = re.sub(r'\\maketitle\b', '', body)
    body = re.sub(r'\\tableofcontents\b', '', body)
    body = re.sub(r'\\pagenumbering\{[^}]*\}', '', body)
    body = re.sub(r'\\pagestyle\{[^}]*\}', '', body)
    body = re.sub(r'\\thispagestyle\{[^}]*\}', '', body)
    body = re.sub(r'\\pagebreak\b', '', body)
    body = re.sub(r'\\clearpage\b', '', body)
    body = re.sub(r'\\cleardoublepage\b', '', body)
    body = re.sub(r'\\makeindex\b', '', body)
    body = re.sub(r'\\makemodindex\b', '', body)

    # Strip TeX dimension/skip assignments that leak into the body
    # e.g. {\parskip = 0mm \tableofcontents} leaves "= 0mm" behind
    body = re.sub(r'\\(?:parskip|parindent|baselineskip|lineskip|topskip'
                  r'|itemsep|parsep|topsep|partopsep|listparindent'
                  r'|labelsep|labelwidth|leftmargin|rightmargin'
                  r'|textwidth|textheight|columnsep|columnwidth'
                  r'|oddsidemargin|evensidemargin|topmargin'
                  r'|headheight|headsep|footskip|marginparsep'
                  r'|marginparwidth)\s*=[^\\{}\n]*', '', body)
    # Remove bare "= XXmm/pt/ex/em" leftovers
    body = re.sub(r'^=\s*-?\d+(?:\.\d+)?\s*(?:mm|cm|pt|in|em|ex|bp|dd|pc)\s*$',
                  '', body, flags=re.MULTILINE)
    # Strip \normalsize, \small, \large etc. font-size commands (bare)
    body = re.sub(r'\\(?:normalsize|small|footnotesize|scriptsize|tiny'
                  r'|large|Large|LARGE|huge|Huge)\b\s*', '', body)
    # Strip \raggedbottom, \sloppy, \noindent, \raggedright etc.
    body = re.sub(r'\\(?:raggedbottom|raggedright|raggedleft|sloppy'
                  r'|flushleft|flushright|centering)\b\s*', '', body)

    # Strip in-body macro/environment definitions -- these conflict with
    # the preamble macros we inject via macros.tex.
    # Patterns: \newcommand{\foo}[n]{...}, \renewcommand, \def\foo, \let\foo\bar
    body = re.sub(r'\\(?:newcommand|renewcommand|providecommand)\s*\*?\s*\{[^}]*\}[^\n]*\n?', '', body)
    body = re.sub(r'\\(?:newcommand|renewcommand|providecommand)\s*\*?\s*\\[a-zA-Z]+[^\n]*\n?', '', body)
    body = re.sub(r'\\(?:newenvironment|renewenvironment)\s*\{[^}]*\}[^\n]*\n?', '', body)
    body = re.sub(r'\\(?:def|gdef|edef|xdef)\s*\\[a-zA-Z]+[^\n]*\n?', '', body)
    body = re.sub(r'\\let\s*\\[a-zA-Z]+\s*[=]?\s*\\[a-zA-Z]+[^\n]*\n?', '', body)

    return body


def strip_comments(text: str) -> str:
    r"""Remove LaTeX line comments (% to end of line), skipping \verb content."""
    result = []
    i = 0
    n = len(text)
    while i < n:
        # Skip \verb|...| or \verb+...+ content (fix_verb runs first)
        if text[i:i+5] == r'\verb' and i + 5 < n and text[i + 5] in '|+':
            delim = text[i + 5]
            end = text.find(delim, i + 6)
            if end != -1:
                result.append(text[i:end + 1])
                i = end + 1
                continue
        # Skip \begin{verbatim}...\end{verbatim}
        if text[i:i+16] == r'\begin{verbatim}':
            end = text.find(r'\end{verbatim}', i + 16)
            if end != -1:
                result.append(text[i:end + 14])
                i = end + 14
                continue
        # Strip % comment (not preceded by \)
        if text[i] == '%' and (i == 0 or text[i - 1] != '\\'):
            while i < n and text[i] != '\n':
                i += 1
            continue
        result.append(text[i])
        i += 1
    return ''.join(result)


def strip_ifhtml(text: str) -> str:
    r"""Remove \ifhtml...\fi blocks (HTML-only content)."""
    # Simple non-nested version; handles most cases
    return re.sub(r'\\ifhtml\b.*?\\fi\b', '', text, flags=re.DOTALL)


def _eat_braced_args(text: str, start: int, max_args: int) -> int:
    """Return the position after eating up to max_args braced args from text[start:]."""
    pos = start
    n = len(text)
    for _ in range(max_args):
        # skip whitespace and optional [...]
        while pos < n and text[pos] in ' \t\n':
            pos += 1
        if pos < n and text[pos] == '[':
            pos += 1
            while pos < n and text[pos] != ']':
                pos += 1
            pos += 1  # skip ']'
            continue
        if pos >= n or text[pos] != '{':
            break
        pos += 1  # skip opening '{'
        depth = 1
        while pos < n and depth:
            if text[pos] == '{':
                depth += 1
            elif text[pos] == '}':
                depth -= 1
            pos += 1
    return pos


def strip_cmds_with_args(text: str, cmd_patterns: list, max_args: int = 4) -> str:
    """
    Strip commands matched by any pattern in cmd_patterns along with their
    subsequent braced (and optional) arguments.  Uses a scan-and-rebuild
    approach so arguments can span multiple lines.
    """
    combined = re.compile('|'.join(cmd_patterns))
    out = []
    pos = 0
    for m in combined.finditer(text):
        if m.start() < pos:
            # this match is inside an already-consumed argument - skip it
            continue
        out.append(text[pos:m.start()])
        end = _eat_braced_args(text, m.end(), max_args)
        pos = end
    out.append(text[pos:])
    return ''.join(out)


def strip_index_cmds(text: str) -> str:
    """Remove index-only LaTeX commands (they produce no visible output)."""
    patterns = [
        r'\\indexii\b', r'\\indexiii\b', r'\\indexiv\b',
        r'\\kwindex\b', r'\\stindex\b', r'\\exindex\b', r'\\obindex\b',
        r'\\bifuncindex\b', r'\\modindex\b', r'\\bimodindex\b',
        r'\\stmodindex\b', r'\\exmodindex\b', r'\\refmodindex\b',
        r'\\refbimodindex\b', r'\\refexmodindex\b', r'\\refstmodindex\b',
        r'\\ttindex\b', r'\\setindexsubitem\b', r'\\withsubitem\b',
        r'\\index\b',
    ]
    return strip_cmds_with_args(text, patterns, max_args=4)


def strip_module_decls(text: str) -> str:
    """Strip module declaration boilerplate."""
    patterns = [r'\\declaremodule\b', r'\\platform\b',
                r'\\sectionauthor\b', r'\\moduleauthor\b',
                r'\\maintainer\b', r'\\modsubindex\b']
    return strip_cmds_with_args(text, patterns, max_args=4)


def fix_tables(text: str) -> str:
    r"""
    Convert simple Python doc table environments to something pandoc can handle.
    The old docs use:
      \begin{tableiii}{l|l|l}{textrm}{Col1}{Col2}{Col3}
      \lineiii{a}{b}{c}
      \end{tableiii}
    Rewrite as a simple tabular so pandoc produces a Markdown table.
    """
    def repl_table(m: re.Match) -> str:
        n = int(m.group(1))        # number of columns
        body = m.group(2)
        cols = ' | '.join(['l'] * n)
        # Replace \lineN{a}{b}... with tabular rows
        def repl_line(lm: re.Match) -> str:
            args = re.findall(r'\{([^}]*)\}', lm.group(0))
            return ' & '.join(args) + r' \\'
        body = re.sub(r'\\line(?:ii|iii|iv)(?:\{[^}]*\}){1,4}', repl_line, body)
        return r'\begin{tabular}{' + cols + r'}' + '\n' + body + r'\end{tabular}'

    text = re.sub(
        r'\\begin\{table(ii|iii|iv)\}[^{]*(?:\{[^}]*\}){2,4}(.*?)\\end\{table(?:ii|iii|iv)\}',
        lambda m: repl_table_generic(m),
        text, flags=re.DOTALL
    )
    return text


def repl_table_generic(m: re.Match) -> str:
    full = m.group(0)
    # Count columns from environment name
    col_match = re.match(r'\\begin\{table(ii+)\}', full)
    if not col_match:
        return full
    n = len(col_match.group(1))  # ii->2, iii->3, iv->4
    # Extract body
    body_match = re.search(r'\}(.*)', full, re.DOTALL)
    if not body_match:
        return full
    body = body_match.group(1).strip()
    # Remove leading {format}{textrm} args
    body = re.sub(r'^\s*\{[^}]*\}\s*\{[^}]*\}', '', body)
    # Convert \lineN{a}{b}... rows
    def repl_line(lm: re.Match) -> str:
        args = re.findall(r'\{([^}]*)\}', lm.group(0))
        return ' & '.join(args[:n]) + r' \\'
    body = re.sub(r'\\line(?:ii|iii|iv)(?:\{[^}]*\})+', repl_line, body)
    cols = ' | '.join(['l'] * n)
    return r'\begin{tabular}{' + cols.replace(' | ', '') + r'}' + '\n' + body.strip() + '\n' + r'\end{tabular}'


def fix_math(text: str) -> str:
    r"""Clean up math expressions.
    - Replace \emph{x} with x inside $ ... $ (not a valid math command).
    - Strip \catcode lines (TeX primitives pandoc can't handle).
    """
    # Strip \catcode`... lines anywhere
    text = re.sub(r'\\catcode[^\n]*', '', text)

    # Replace \emph{x} -> x inside inline math $...$
    def clean_inline_math(m: re.Match) -> str:
        content = re.sub(r'\\emph\{([^}]*)\}', r'\1', m.group(1))
        return '$' + content + '$'
    text = re.sub(r'\$([^$\n]{1,200})\$', clean_inline_math, text)

    return text


def fix_unmatched_braces(text: str) -> str:
    """Remove closing braces that have no matching open brace."""
    # First pass: collect positions of unmatched '}'
    depth = 0
    unmatched = []
    in_verbatim = False
    i = 0
    while i < len(text):
        # crude verbatim detection: skip \begin{verbatim}...\end{verbatim}
        if text[i:i+16] == r'\begin{verbatim}':
            end = text.find(r'\end{verbatim}', i + 16)
            if end != -1:
                i = end + 14
                continue
        if text[i] == '{' and (i == 0 or text[i-1] != '\\'):
            depth += 1
        elif text[i] == '}' and (i == 0 or text[i-1] != '\\'):
            if depth > 0:
                depth -= 1
            else:
                unmatched.append(i)
        i += 1
    if not unmatched:
        return text
    # Remove unmatched positions (in reverse order to preserve indices)
    chars = list(text)
    for pos in reversed(unmatched):
        chars[pos] = ''
    return ''.join(chars)


def process(path: str, base_dir: str) -> str:
    text = read_file(path)
    text = expand_inputs(text, base_dir)
    text = fix_verb(text)
    text = strip_comments(text)
    text = strip_doc_structure(text)
    text = strip_ifhtml(text)
    text = strip_index_cmds(text)
    text = strip_module_decls(text)
    text = fix_tables(text)
    text = fix_math(text)
    text = fix_unmatched_braces(text)
    return text


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    src = sys.argv[1]
    base = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(src))
    print(process(src, base))
