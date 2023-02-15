Simple django project with custom functionalities to default django auth:
- Restricts registration to email/email domains that are whitelisted in the admin backend.
- Domains are whitelisted by adding domain e.g. domain.com in the admin section


To run:
1. install python dependencies - pip install -m requirements.txt
2. create database - python manage.py migrate
3. start django server - python manage.py runserver
