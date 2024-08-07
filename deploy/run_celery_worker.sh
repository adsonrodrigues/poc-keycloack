#!/bin/bash
set -e

cd /app
celery -A core worker --loglevel info