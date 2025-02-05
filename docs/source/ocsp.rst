####################
Run a OCSP responder
####################

Hosting an OCSP service is the second method (besides :doc:`CRLs <crl>`) of
letting a client know if a certificate has been revoked.

**django-ca** does not provide a way to host an OCSP service itself, but all
other necessary parts are included, if you intend to run such a service.

************************************
Create an OCSP responser certificate
************************************

To run an OCSP responder, you first need a certificate with some special
properties. Luckily, **django-ca** has a profile predefined for you:

.. code-block:: console

   $ openssl genrsa -out ocsp.key 4096
   $ openssl req -new -key ocsp.key -out ocsp.csr -utf8 -batch
   $ python manage.py sign_cert --csr=ocsp.csr --out=ocsp.pem \
   >     --subject /CN=ocsp.example.com --ocsp


********************************
Add OCSP URL to new certificates
********************************

To include the URL to an OCSP service to newly issued certificates (you cannot
add it to already issued certificates, obviously), either set it in the admin
interface or via the command line:

.. code-block:: console

   $ python manage.py list_cas
   34:D6:02:B5:B8:27:4F:51:9A:16:0C:B8:56:B7:79:3F - Root CA
   $ python manage.py edit_ca --ocsp-url=http://ocsp.example.com/ \
   >     34:D6:02:B5:B8:27:4F:51:9A:16:0C:B8:56:B7:79:3F

*******************************************
Run an OCSP responser with ``openssl ocsp``
*******************************************

OpenSSL ships with the ``openssl ocsp`` command that allows you to run an OCSP
responser, but note that the manpage says **"only useful for test and
demonstration purposes"**.

To use the command, generate an index:

.. code-block:: console

   $ python manage.py dump_ocsp_index ocsp.index

OpenSSL itself allows you to run an OCSP responder with this command:

.. code-block:: console

   $ openssl ocsp -index ocsp.index -port 8888 -rsigner ocsp.pem \
   >     -rkey ocsp.example.com.key -CA files/ca.crt -text
