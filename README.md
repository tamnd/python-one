# python-one

Source archive of every Python release from 1.0.1 (February 1994) through 2.0c1 (October 2000), extracted from the original tarballs at [legacy.python.org/download/releases/src](https://legacy.python.org/download/releases/src/).

Each version lives under `src/<version>/` exactly as it shipped. Every version was added by its own pull request, committed as close as possible to the original release date. That means you can `git log` the repo and watch Python's history unfold chronologically, diff one release against the next, and browse the source on GitHub without downloading anything.

**Browsable documentation:** [tamnd.github.io/python-one](https://tamnd.github.io/python-one/)

---

## Versions

### 1.0.1 -- February 1994

The first publicly available stable release. Guido van Rossum had been working on Python at CWI (Amsterdam) since 1989. By 1.0, the language had exceptions, functions, modules, classes, and a small standard library. 1.0.1 was a portability patch -- fixes for SunOS, SGI, HP-UX, and a few crash bugs found right after 1.0 shipped.

The entire parser, compiler, and runtime fit in a few thousand lines of C. There is no garbage collector beyond reference counting. There are no Unicode strings. The `Misc/HISTORY` file mentions Guido's original motivation: he wanted a language that could replace shell scripts but felt more like C.

### 1.1 -- October 1994

Adds `__getitem__` and `__setitem__` for operator overloading. The `Tkinter` binding for Tk arrives for the first time (it lived outside the standard library before this). Dynamic loading of extension modules on systems that support `dlopen()`. The `os` module gets `path.walk`. A few hundred lines of new library code.

This is also when `sys.exc_info()` appeared, replacing the older `sys.exc_type` / `sys.exc_value` pair that scripts were still using into the late 1990s.

### 1.2 -- April 1995

`pickle` and `shelve` arrive. `import a.b.c` package syntax is added (though the `__init__.py` convention was already in use informally). `struct` gets format characters for unsigned types. The `re` module is still the old `regex` engine at this point -- Spencer regexes, not the PCRE-style SRE that would come in 1.6.

Guido moved from CWI to CNRI in Reston, Virginia around this time. The copyright notices in the source shift from CWI to CNRI starting with the releases that follow.

### 1.3 -- October 1995

Keyword arguments become part of the language. Before this you could accept `**kwargs` but there was no syntax for calling `f(key=value)` in a way the interpreter handled natively. The `copy` module arrives. `string` gets `atoi`, `atof`, `atol`. `sys.version_info` (a named tuple) is new here.

The `Doc/` tree in this release is written entirely in LaTeX, the format Python used for all documentation through 2.0.

### 1.4 -- October 1996

The `Universal Makefile.pre.in` framework for building extension modules outside the CPython source tree is introduced. This is the ancestor of `distutils`. Private name mangling (`__foo` becoming `_ClassName__foo`) arrives. `complex` numbers become a built-in type. `ni` (nested imports, the predecessor of packages) is dropped -- the real package import system is now built in.

The release also adds `keyword` and `pprint` to the standard library.

### 1.5 -- December 1997

A major release. Package imports (`import foo.bar`) are fully supported. The `-O` optimization flag strips `assert` statements and `__doc__` strings. The `re` module gets a new interface (still the old Spencer backend, but the API is stabilized). `sys.path` initialization is rationalized. 64-bit fixes throughout. The `threading` module arrives.

`Misc/HISTORY` describes this as the release where Python "came of age" for large-scale use. Several commercial projects were by this point built on Python 1.4/1.5.

### 1.5.1 -- April 1998

Mostly a bug fix release: bare `raise` to re-raise the current exception, `threaded import` locking to fix import races, and tab/space mixing warnings. No `Doc/` directory -- the documentation was distributed separately for these pre-releases.

### 1.5.2 series -- late 1998 through April 1999

Five releases: 1.5.2b1, 1.5.2b2, 1.5.2c1, and 1.5.2. Highlights: `NotImplementedError`, the `winsound` module, `-OO` stripping docstrings, `sha` module, Win/CE threads. The `zlib` inflate fix in 1.5.2c1 was a real security issue for anyone using compressed streams over the network. None of these include a `Doc/` tree either.

1.5.2 stayed the recommended production release for a long time after 1.6 and even 2.0 shipped, because of its stability and wide OS support.

### 1.6b1 / 1.6 -- August/September 2000

The last release from CNRI. Unicode support lands as a built-in type (`u"..."` literals, `unicode()`, `unicodedata`). String methods (`str.split()`, `str.join()`, etc.) replace the old `string` module functions. The SRE regex engine by Fredrik Lundh replaces the ancient Spencer implementation -- this is the `re` module that Python still uses today.

The doc tree switches to a subdirectory layout (`tut/`, `lib/`, `ref/`, `ext/`, `api/`, `inst/`, `dist/`, `mac/`) to handle the volume of documentation.

1.6 was released the same day as 2.0b1, which made for a confusing few weeks.

### 2.0b1 -- September 2000

Guido and the core team had moved to BeOpen.com to form PythonLabs. The first beta brings list comprehensions (`[x*2 for x in range(10)]`), augmented assignment (`+=`, `-=`, etc.), `zip()` as a built-in, and the start of a proper `distutils` in the standard library (version 0.9.3).

### 2.0b2 -- September 2000

Unbounded integer format strings (`%d` on a `long` no longer truncates). `distutils` bumped to 0.9.3. A few encoding fixes in the new Unicode handling.

### 2.0c1 -- October 2000

Release candidate. Bug fixes, Unicode cleanup, the final pre-release before Python 2.0. This is the last version in this archive.

---

## Docs

The documentation site at [tamnd.github.io/python-one](https://tamnd.github.io/python-one/) converts the original LaTeX sources in `src/*/Doc/` to Markdown via pandoc, then builds a searchable Hugo Book site. Each version that ships a `Doc/` tree gets a full set of pages: tutorial, library reference, language reference, C API, and more.

The conversion pipeline lives in `scripts/make-docs/`. See [scripts/make-docs/README.md](scripts/make-docs/README.md) for how it works.

---

## Layout

```
src/<version>/        extracted source tree for that release
scripts/download.sh   fetch all tarballs from legacy.python.org
scripts/extract.sh    extract each tarball into src/<version>/
scripts/make-docs/    LaTeX-to-Markdown conversion pipeline
site/                 Hugo site source
```

## Rebuilding

```sh
scripts/download.sh   # fetch tarballs into _downloads/
scripts/extract.sh    # extract into src/<version>/
```

To regenerate the docs site:

```sh
scripts/make-docs/convert.sh
cd site && hugo server
```

Requires `uv` and `pandoc 3.x`. See `scripts/make-docs/README.md`.

## License

Source code in `src/` is under the terms in `LICENSE` (the stacked CWI + CNRI + BeOpen license from Python 2.0). Everything else in this repo is public domain / CC0.
