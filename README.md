# python-one

A source archive of historical Python releases, from 1.0.1 up to 2.0c1, mirrored
from [legacy.python.org/download/releases/src](https://legacy.python.org/download/releases/src/).
Each release lives under `src/<version>/` with its files extracted exactly as they
shipped, and each version was introduced by its own pull request committed at (or as
close as possible to) the original release date.

The goal is to make it easy to browse the old sources on GitHub, diff one release
against the next, and watch the language grow from a small CWI project into
Python 2.

## Versions

| Version  | Released   |
| -------- | ---------- |
| 1.0.1    | 1994-02-15 |
| 1.1      | 1994-10-11 |
| 1.2      | 1995-04-10 |
| 1.3      | 1995-10-12 |
| 1.4      | 1996-10-25 |
| 1.5      | 1997-12-31 |
| 1.5.1    | 1998-04-14 |
| 1.5.2b1  | 1998-12-23 |
| 1.5.2b2  | 1999-02-19 |
| 1.5.2c1  | 1999-04-09 |
| 1.5.2    | 1999-04-14 |
| 1.6b1    | 2000-08-05 |
| 1.6      | 2000-09-05 |
| 2.0b1    | 2000-09-06 |
| 2.0b2    | 2000-09-27 |
| 2.0c1    | 2000-10-10 |

## Layout

```
src/<version>/    extracted source tree for that release
scripts/          helpers that download and extract the tarballs
LICENSE           the stacked CWI + CNRI + BeOpen license from Python 2.0
README.old        the original README from legacy.python.org/download/releases/src
```

## Rebuilding the archive from scratch

```sh
scripts/download.sh   # fetch every tarball into _downloads/
scripts/extract.sh    # extract each into src/<version>/
```

## License

The code in `src/` is distributed under the terms of the `LICENSE` file in this
repo, which is the license shipped with Python 2.0.
