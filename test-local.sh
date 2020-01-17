#!/usr/bin/env bash
set -o errexit
set -o pipefail

./test-ci.sh
./download-data.sh
./build-and-run-image.sh
# TODO: Make assertion about output.

cd webapp
./start.sh
# TODO: Wait for Flask to start and check response.
