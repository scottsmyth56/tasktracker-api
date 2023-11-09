release: python manage.py makemigrations && python manage.py migrate
web: gunicorn tasktracker_api.wsgi
