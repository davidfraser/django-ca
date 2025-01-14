# django-ca

**django-ca** is a small project to manage TLS certificate authorities and easily issue
certificates.  It is based on [pyOpenSSL](https://pyopenssl.readthedocs.org/) and
[Django](https://www.djangoproject.com/>). It can be used as an app in an existing Django project
or stand-alone with the basic project included.  Certificates can be managed through Djangos admin
interface or via `manage.py` commands - so no webserver is needed, if you’re happy with the
command-line.

Documentation is available at http://django-ca.readthedocs.org/.

## Features

1. Set up a secure local certificate authority in just a few minutes.
2. Written in Python2.7/Python3.4+.
3. Manage your entire certificate authority from the command line and/or via
   Djangos admin interface.
4. Get email notifications about certificates about to expire.
5. Support generating for certificate revocation lists (CRLs).
6. Generates index files that can be used with the `openssl ocsp` command for a crude OCSP service.
7. Display Serial in view_(cert,ca) commands.

Please see https://django-ca.readthedocs.org for more extensive documentation.

## Documentation

Documentation is available at http://django-ca.readthedocs.org/.

## ChangeLog

Please see http://django-ca.readthedocs.io/en/latest/changelog.html

## ToDo

Ideas on what we could do for future releases:

1. Only send out one notification if multiple certificates expire for a user.
2. Add a "renew" button in the admin interface.
3. Add ability to automatically regenerate CRLs when a certificate is revoked.
4. Add a OCSP service maybe (would be huge).
5. Add ability to download PEM/DER of certificates and the CA.

## License

This project is free software licensed under the [GPLv3](http://www.gnu.org/licenses/gpl.txt).
