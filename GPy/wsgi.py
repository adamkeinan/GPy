"""
WSGI config for PyBeacon project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import environ
import os

from django.core.wsgi import get_wsgi_application

environ.env.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
