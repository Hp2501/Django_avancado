"""
WSGI config for djangoavancado project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# Heroku
from dj_static import Cling, MediaCling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoavancado.settings')

# Estáticos e Arquivos de Media (Heroku)
application = Cling(MediaCling(get_wsgi_application()))
#application = get_wsgi_application()
