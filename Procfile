web: gunicorn simplesocial.wsgi --log-file  - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate