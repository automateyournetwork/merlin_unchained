from waitress import serve
from merlin.wsgi import application


serve(application, listen='*:8000', threads=8)