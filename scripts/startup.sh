cd merlin
python3 manage.py makemigrations merlin
python3 manage.py migrate merlin
python3 manage.py migrate
python3 manage.py collectstatic --noinput
python3 manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL
redis-server --daemonize yes 
redis-cli ping
python3 waitress_server.py