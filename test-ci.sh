#!/usr/bin/env bash
set -o errexit
set -o pipefail

die() { set +v; echo "$*" 1>&2 ; exit 1; }

flake8 || die 'Try "autopep8 --in-place --aggressive -r ."'

pytest
