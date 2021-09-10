# merlin_unchained
A Django implementation of Merlin


1. Create Project
2. Makemigrations
3. Migrate 
4. Migrate
5. Superuser 
6. populate 

export DJANGO_SETTINGS_MODULE=merlin.settings

pkill -f "celery worker"  
celery -A merlin beat -l info --logfile=celery.beat.log --detach  
celery -A merlin worker -l info --logfile=celery.log --detach

kill -9 $(ps aux | grep celery | grep -v grep | awk '{print $2}' | tr '\n'  ' ') > /dev/null 2>&1