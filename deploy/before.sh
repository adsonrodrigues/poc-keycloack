#!/bin/bash
python3 /app/manage.py migrate  --noinput
python3 /app/manage.py collectstatic --no-input
# locale-gen "pt_BR.UTF-8"