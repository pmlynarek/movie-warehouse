#!/bin/sh

python manage.py collectstatic --no-input || exit 1
echo "collectstatic finished successfully"
