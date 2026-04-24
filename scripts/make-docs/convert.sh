#!/bin/sh
# Convert all Python version LaTeX docs to Hugo Markdown.
# Run from the repo root: scripts/make-docs/convert.sh
#
# Requirements: uv (https://github.com/astral-sh/uv), pandoc 3.x
# uv handles the Python environment; no need to install anything manually.
set -eu

REPO="$(cd "$(dirname "$0")/../.." && pwd)"
SCRIPTS="$REPO/scripts/make-docs"
CONTENT="$REPO/site/content/docs"
PREAMBLE="$SCRIPTS/macros.tex"

die() { echo "ERROR: $*" >&2; exit 1; }
need() { command -v "$1" >/dev/null 2>&1 || die "missing: $1"; }

need uv
need pandoc

# Run preprocess.py via uv so the right Python version is always used
PY="uv run --project $SCRIPTS python"

# ---------------------------------------------------------------------------
# Helper: convert one .tex file to Markdown via pandoc.
# Returns pandoc output on stdout. Exits 0 even on pandoc error (empty output).
# Usage: _run_pandoc <input.tex> <base_dir>
# ---------------------------------------------------------------------------
_run_pandoc() {
    src="$1"; base="$2"
    tmpfile="$(mktemp /tmp/pydoc-XXXXXX.tex)"
    {
        printf '\\documentclass{article}\n'
        cat "$PREAMBLE"
        printf '\\begin{document}\n'
        $PY "$SCRIPTS/preprocess.py" "$src" "$base"
        printf '\n\\end{document}\n'
    } > "$tmpfile"
    pandoc \
        --from=latex \
        --to=gfm \
        --wrap=none \
        --syntax-highlighting=none \
        "$tmpfile" 2>/dev/null || true
    rm -f "$tmpfile"
}

# ---------------------------------------------------------------------------
# Helper: convert one top-level .tex file to .md
# For library docs in subdir layout, expands each lib*.tex individually
# and concatenates, to avoid brace-balance issues across 200+ files.
# Usage: tex_to_md <input.tex> <output.md> <title> <weight> [lib_subdir]
# ---------------------------------------------------------------------------
tex_to_md() {
    src="$1"; dest="$2"; title="$3"; weight="$4"
    lib_subdir="${5:-}"
    mkdir -p "$(dirname "$dest")"
    base="$(dirname "$src")"

    # Prepend Hugo front matter
    {
        printf -- '---\ntitle: "%s"\nweight: %s\n---\n\n' "$title" "$weight"

        if [ -n "$lib_subdir" ] && [ -d "$lib_subdir" ]; then
            # Process each lib*.tex (or *.tex) file individually to avoid
            # cumulative brace-balance errors in the concatenated mega-file.
            # The master lib.tex may have intro content too.
            _run_pandoc "$src" "$base"
            find "$lib_subdir" -maxdepth 1 -name 'lib*.tex' | sort | while read -r f; do
                _run_pandoc "$f" "$lib_subdir"
            done
        else
            _run_pandoc "$src" "$base"
        fi

        printf '\n\n{{< python-copyright version="%s" >}}\n' "$ver"
    } > "$dest"

    echo "  wrote $dest"
}

# ---------------------------------------------------------------------------
# Helper: for early versions where lib.tex \input{}'s all lib*.tex
# We just need to run preprocess on lib.tex (which expands inputs)
# Same for ref.tex -> ref[1-8].tex
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Helper: for 1.6+ where docs are in subdirectories
# find_main_tex <doc_subdir> <expected_main_name>
# ---------------------------------------------------------------------------
find_main_tex() {
    dir="$1"; main="$2"
    if [ -f "$dir/$main.tex" ]; then
        echo "$dir/$main.tex"
    elif [ -f "$dir/$main" ]; then
        # directory case e.g. ref/ with ref.tex inside
        find "$dir/$main" -maxdepth 1 -name "$main.tex" | head -1
    else
        echo ""
    fi
}

# ---------------------------------------------------------------------------
# Build one version
# ---------------------------------------------------------------------------
build_version() {
    ver="$1"
    src_doc="$REPO/src/$ver/Doc"
    out="$CONTENT/$ver"
    mkdir -p "$out"

    echo "=== $ver ==="

    # Version _index.md
    cat > "$out/_index.md" << HEREDOC
---
title: "Python $ver"
weight: $(version_weight "$ver")
bookCollapseSection: true
---

# Python $ver

Documentation extracted from the \`src/$ver/Doc/\` tree of the original
tarball. See also: [source code](https://github.com/tamnd/python-one/tree/main/src/$ver/).
HEREDOC

    # Determine layout: flat (pre-1.6) vs subdir (1.6+)
    if [ -d "$src_doc/tut" ]; then
        layout="subdir"
    else
        layout="flat"
    fi

    # Tutorial
    if [ "$layout" = "subdir" ] && [ -f "$src_doc/tut/tut.tex" ]; then
        tex_to_md "$src_doc/tut/tut.tex" "$out/tutorial.md" "Tutorial" 10
    elif [ -f "$src_doc/tut.tex" ]; then
        tex_to_md "$src_doc/tut.tex" "$out/tutorial.md" "Tutorial" 10
    fi

    # Library reference (process each lib*.tex individually for subdir layout)
    if [ "$layout" = "subdir" ] && [ -f "$src_doc/lib/lib.tex" ]; then
        tex_to_md "$src_doc/lib/lib.tex" "$out/library.md" "Library Reference" 20 "$src_doc/lib"
    elif [ -f "$src_doc/lib.tex" ]; then
        tex_to_md "$src_doc/lib.tex" "$out/library.md" "Library Reference" 20
    fi

    # Language reference
    if [ "$layout" = "subdir" ] && [ -d "$src_doc/ref" ]; then
        main=$(find "$src_doc/ref" -maxdepth 1 -name "ref.tex" | head -1)
        [ -n "$main" ] && tex_to_md "$main" "$out/reference.md" "Language Reference" 30
    elif [ -f "$src_doc/ref.tex" ]; then
        tex_to_md "$src_doc/ref.tex" "$out/reference.md" "Language Reference" 30
    elif [ -f "$src_doc/ref1.tex" ]; then
        # 1.0.1-1.4 style: ref.tex split across ref1.tex...ref8.tex
        # Build a synthetic top-level that inputs them all
        tmpref="$(mktemp /tmp/pydocref-XXXXXX.tex)"
        printf '\\documentclass{article}\n\\begin{document}\n' > "$tmpref"
        for n in 1 2 3 4 5 6 7 8; do
            [ -f "$src_doc/ref${n}.tex" ] && printf '\\input{ref%s}\n' "$n" >> "$tmpref"
        done
        printf '\\end{document}\n' >> "$tmpref"
        tex_to_md "$tmpref" "$out/reference.md" "Language Reference" 30
        rm -f "$tmpref"
    fi

    # Extending and embedding
    if [ "$layout" = "subdir" ] && [ -f "$src_doc/ext/ext.tex" ]; then
        tex_to_md "$src_doc/ext/ext.tex" "$out/extending.md" "Extending and Embedding" 40
    elif [ -f "$src_doc/ext.tex" ]; then
        tex_to_md "$src_doc/ext.tex" "$out/extending.md" "Extending and Embedding" 40
    fi

    # C API (1.5+)
    if [ "$layout" = "subdir" ] && [ -d "$src_doc/api" ]; then
        main=$(find "$src_doc/api" -maxdepth 1 -name "api.tex" | head -1)
        [ -n "$main" ] && tex_to_md "$main" "$out/api.md" "Python/C API" 50
    elif [ -f "$src_doc/api.tex" ]; then
        tex_to_md "$src_doc/api.tex" "$out/api.md" "Python/C API" 50
    fi

    # Installing (1.6+)
    if [ "$layout" = "subdir" ] && [ -d "$src_doc/inst" ]; then
        main=$(find "$src_doc/inst" -maxdepth 1 -name "inst.tex" | head -1)
        [ -n "$main" ] && tex_to_md "$main" "$out/installing.md" "Installing Python Modules" 60
    fi

    # Distributing (1.6+)
    if [ "$layout" = "subdir" ] && [ -d "$src_doc/dist" ]; then
        main=$(find "$src_doc/dist" -maxdepth 1 -name "dist.tex" | head -1)
        [ -n "$main" ] && tex_to_md "$main" "$out/distributing.md" "Distributing Python Modules" 70
    fi

    # Macintosh library (1.6+)
    if [ "$layout" = "subdir" ] && [ -d "$src_doc/mac" ]; then
        main=$(find "$src_doc/mac" -maxdepth 1 -name "mac.tex" | head -1)
        [ -n "$main" ] && tex_to_md "$main" "$out/macintosh.md" "Macintosh Library Modules" 80 "$src_doc/mac"
    fi
}

# Map version string to a numeric sort weight for Hugo sidebar order
version_weight() {
    case "$1" in
        1.0.1)    echo 101 ;;
        1.1)      echo 110 ;;
        1.2)      echo 120 ;;
        1.3)      echo 130 ;;
        1.4)      echo 140 ;;
        1.5)      echo 150 ;;
        1.5.1)    echo 151 ;;
        1.5.2b1)  echo 152 ;;
        1.5.2b2)  echo 153 ;;
        1.5.2c1)  echo 154 ;;
        1.5.2)    echo 155 ;;
        1.6b1)    echo 160 ;;
        1.6)      echo 161 ;;
        2.0b1)    echo 200 ;;
        2.0b2)    echo 201 ;;
        2.0c1)    echo 202 ;;
        *)        echo 999 ;;
    esac
}

# ---------------------------------------------------------------------------
# Main: iterate over all versions that have a Doc/ dir
# ---------------------------------------------------------------------------
cd "$REPO"

VERSIONS="1.0.1 1.1 1.2 1.3 1.4 1.5 1.5.1 1.5.2b1 1.5.2b2 1.5.2c1 1.5.2 1.6b1 1.6 2.0b1 2.0b2 2.0c1"

for ver in $VERSIONS; do
    if [ -d "$REPO/src/$ver/Doc" ]; then
        build_version "$ver"
    else
        echo "  skip $ver (no Doc/)"
    fi
done

echo ""
echo "Done. Run: cd site && hugo server"
