#!/bin/sh
# Download every historical Python tarball covered by this archive into _downloads/.
# Re-runs are cheap: curl -O is skipped if the file already exists.

set -eu

cd "$(dirname "$0")/.."
mkdir -p _downloads
cd _downloads

BASE="https://legacy.python.org/download/releases/src"

FILES="
python1.0.1.tar.gz
python1.1.tar.gz
python-1.2.tar.gz
python-1.3.tar.gz
python-1.4.tar.gz
python-1.5.tar.gz
python-1.5.1.tar.gz
python-1.5.2b1.tar.gz
python-1.5.2b2.tar.gz
python-1.5.2c1.tar.gz
python-1.5.2.tar.gz
python-1.6b1.tar.gz
python-1.6.tar.gz
python-2.0b1.tar.gz
python-2.0b2.tar.gz
python-2.0c1.tar.gz
"

for f in $FILES; do
	if [ -f "$f" ]; then
		echo "have  $f"
	else
		echo "fetch $f"
		curl -fSsO "$BASE/$f"
	fi
done
