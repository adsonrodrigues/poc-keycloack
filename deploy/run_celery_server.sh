#!/bin/bash
set -e

cd /app
celery -A core beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler