#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

python infoweb/manage.py collectstatic --no-input
python infoweb/manage.py migrate
