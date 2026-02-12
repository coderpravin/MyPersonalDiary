#!/usr/bin/env bash
set -o errexit

pip install -r reqquirements.txt
python manage.py collectstatic
python manage.py migrate 

