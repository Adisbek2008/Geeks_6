#!/bin/bash
# entrypoint.sh

python manage.py migrate --noinput

python manage.py collectstatic --noinput

gunicorn geeks6.wsgi:application --bind 0.0.0.0:8000 --workers 4
