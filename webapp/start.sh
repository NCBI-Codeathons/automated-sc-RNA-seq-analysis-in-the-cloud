#!/usr/bin/env bash
set -o errexit
set -o pipefail

export FLASK_APP=app
export FLASK_ENV=development

flask run
