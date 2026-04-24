# make-docs

Converts the original Python LaTeX documentation (from each `src/<version>/Doc/` tree) into Hugo-compatible Markdown files under `site/content/docs/`.

## Requirements

- [uv](https://github.com/astral-sh/uv) -- handles the Python environment automatically, no manual `pip install` needed
- [pandoc](https://pandoc.org/) 3.x

Install pandoc on macOS:

```sh
brew install pandoc
```

## Usage

Run from the repo root:

```sh
scripts/make-docs/convert.sh
```

Output goes to `site/content/docs/<version>/`. After that:

```sh
cd site && hugo server
```

## How it works

`convert.sh` iterates over every Python version that has a `Doc/` directory and calls `tex_to_md()` for each document type (tutorial, library reference, language reference, etc.).

For each `.tex` file it:

1. Runs `preprocess.py` to expand `\input{}` includes, fix up old `\verb\text\` syntax, strip LaTeX boilerplate that pandoc can not handle, and convert Python-specific table environments to standard `tabular`.
2. Wraps the result in a minimal `\documentclass{article}` + `macros.tex` preamble.
3. Passes that to pandoc (`--from=latex --to=gfm`) to produce GitHub Flavored Markdown.
4. Prepends Hugo front matter and appends a copyright notice shortcode.

The library reference for 1.6+ is split across ~200 individual `lib*.tex` files. Those are processed one at a time and concatenated, rather than merged into a single file first. This avoids brace-balance errors that accumulate across that many files.

### Versions covered

All versions that ship a `Doc/` directory in their tarball:

| Version | Layout |
|---------|--------|
| 1.0.1, 1.1, 1.2, 1.3, 1.4, 1.5 | flat (`tut.tex`, `lib.tex`, `ref1.tex`...) |
| 1.6b1, 1.6 | subdirectories (`tut/`, `lib/`, `ref/`, `ext/`, `api/`, `inst/`, `dist/`, `mac/`) |
| 2.0b1, 2.0b2, 2.0c1 | same subdir layout as 1.6 |

Versions 1.5.1, 1.5.2b1, 1.5.2b2, 1.5.2c1, 1.5.2 do not include a `Doc/` tree and are skipped.

### Files

| File | Purpose |
|------|---------|
| `convert.sh` | Main orchestrator |
| `preprocess.py` | LaTeX preprocessor |
| `macros.tex` | Pandoc preamble that maps Python-specific macros to standard LaTeX |
| `pyproject.toml` | uv project file pinning Python 3.12+ |
