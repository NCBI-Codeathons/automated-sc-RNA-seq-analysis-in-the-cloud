#!/usr/bin/env bash
set -o errexit
set -o pipefail

wget files from figshare and write in the correct directory
build Dockerimage
run Dockerimage with the files we have pulled down
check output is what we want the output to be
