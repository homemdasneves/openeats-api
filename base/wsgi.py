#!/usr/bin/env python
# encoding: utf-8

"""
WSGI config for base project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "base.settings")

application = get_wsgi_application()

