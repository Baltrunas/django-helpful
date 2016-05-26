from __future__ import unicode_literals

from django.apps import AppConfig


class HelpfulConfig(AppConfig):
    name = 'helpful'

from . import signals
