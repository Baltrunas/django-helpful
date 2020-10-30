A handful of utilities for Django!
==================================

.. image:: https://img.shields.io/pypi/v/django-helpful.svg
    :target: https://pypi.python.org/pypi/django-helpful
    :alt: Latest PyPI version
.. image:: https://img.shields.io/pypi/dm/django-helpful.svg
    :target: https://pypi.python.org/pypi/django-helpful
    :alt: Number of PyPI downloads
.. image:: https://img.shields.io/pypi/l/django-helpful.svg
    :target: https://pypi.python.org/pypi/django-helpful


*******
Install
*******

* Copy to helpful or include as git submodule
* Add ```'helpful',``` to ```INSTALLED_APPS ```
* Add ```EMAIL_DEBUG = ['debug@email.com']``` to ```settings.py``` for use debug email mode. (chanhe email address)
* Add ```EMAIL_DEBUG_INFO = True``` to ```settings.py``` to show debug info (original email address) before email


Template Tags
-------------

image2base64
^^^^^^^^^^^^
convert image to base64

.. code-block:: html

    {% image2base64 "image.png" %}

object_dict
^^^^^^^^^^^
.. code-block:: html

    {% load object_dict %}
    {% for field in message|object_dict %}
        {{ field.verbose_name }}
        {{ field.display }}
    {% endfor %}

abs_puth
^^^^^^^^
.. code-block:: html

    {% load abs_puth %}
    {% abs_puth "static" "django/img/logo.png" %}
    {% abs_puth "media" "uploads/photos/joue.jpg" %}
    {% abs_puth "base" "templates/e-mail/css/style.css" %}
    {% abs_puth "parent" "extra/logo.png" %}


easy_email
==========

template must be 'email/contacts'
files 'email/contacts.html' and 'email/contacts.txt'
must will exist

.. code-block:: python

    from helpful.easy_email import mail
    mail(subject, context, template, from_email, to_email, connection=None, reply_to=None, attach_files=[], cc=None, bcc=None)
