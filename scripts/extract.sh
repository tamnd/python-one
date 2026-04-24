#!/bin/sh
# Extract each tarball from _downloads/ into src/<version>/.
# The archive's top-level directory varies in case (python-1.0.1 vs Python-2.0c1)
# so we extract to a temp spot and then move the one child into place.

set -eu

cd "$(dirname "$0")/.."
mkdir -p src

# tarball : target version directory
MAP="
python1.0.1.tar.gz:1.0.1
python1.1.tar.gz:1.1
python-1.2.tar.gz:1.2
python-1.3.tar.gz:1.3
python-1.4.tar.gz:1.4
python-1.5.tar.gz:1.5
python-1.5.1.tar.gz:1.5.1
python-1.5.2b1.tar.gz:1.5.2b1
python-1.5.2b2.tar.gz:1.5.2b2
python-1.5.2c1.tar.gz:1.5.2c1
python-1.5.2.tar.gz:1.5.2
python-1.6b1.tar.gz:1.6b1
python-1.6.tar.gz:1.6
python-2.0b1.tar.gz:2.0b1
python-2.0b2.tar.gz:2.0b2
python-2.0c1.tar.gz:2.0c1
"

for entry in $MAP; do
	tarball="${entry%%:*}"
	version="${entry##*:}"
	dest="src/$version"
	if [ -d "$dest" ]; then
		echo "have  $dest"
		continue
	fi
	if [ ! -f "_downloads/$tarball" ]; then
		echo "missing _downloads/$tarball (run scripts/download.sh first)" >&2
		exit 1
	fi
	echo "unpack $tarball -> $dest"
	tmp="$(mktemp -d)"
	tar -xzf "_downloads/$tarball" -C "$tmp"
	inner="$(ls "$tmp")"
	mv "$tmp/$inner" "$dest"
	rmdir "$tmp"
done
