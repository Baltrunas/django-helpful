# A handful of utilities for Django!

.. image:: https://img.shields.io/pypi/v/django-helpful.svg
    :target: https://pypi.python.org/pypi/django-helpful
    :alt: Latest PyPI version
.. image:: https://img.shields.io/pypi/dm/django-helpful.svg
    :target: https://pypi.python.org/pypi/django-helpful
    :alt: Number of PyPI downloads
.. image:: https://img.shields.io/pypi/l/django-helpful.svg
    :target: https://pypi.python.org/pypi/django-helpful

# Install
* Copy to helpful or include as git submodule
* Add ```'helpful',``` to ```INSTALLED_APPS ```

## Template Tags
### image2base64
convert image to base64
```
{% image2base64 "image.png" %}
```

### object_dict
```
{% load object_dict %}
{% for field in message|object_dict %}
	{{ field.verbose_name }}
	{{ field.display }}
{% endfor %}
```

### abs_puth
```
{% load abs_puth %}
{% abs_puth "static" "templates/e-mail/css/style.css" %}
{% abs_puth "media" "templates/e-mail/css/style.css" %}
{% abs_puth "base" "templates/e-mail/css/style.css" %}
{% abs_puth "parent" "templates/e-mail/css/style.css" %}
```

# easy_email
template must be 'email/contacts'
files 'email/contacts.html' and 'email/contacts.txt'
must will exist
```
from helpful.easy_email import mail
mail(subject, context, template, from_email, to_email, connection=None)
```