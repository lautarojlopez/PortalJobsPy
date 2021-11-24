# PortalJobsPy
Job search website example developed using Django. Project still on progress.

# Notes
For te project to work correctly, it is necessary to create the 'hstore' extension in Postgres.  
``$ sudo -u postgres psql``  
``postgres=# CREATE EXTENSION hstore;``  

Users are able to create two types of accounts, 'Postulante' and 'Reclutador'.
The 'Postulante' type allow users to create their own CV's (resume) and fill it with their personal data, in order to be able to postulate to job offers.
The 'Reclutador' type allow users to create publications for job offers, where other users are able to postulate.
