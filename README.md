# REST API for sending emails

### To run locally
Clone the repository

`git clone <url>`

`cd restapi-mail`

Create a virtual environment

`python3.10 -m venv env`

`source env/bin/activate`

Install dependencies

`pip install -r requirements.txt`

Create a database and an .env file with the path to the database

`createdb <database_name>`

`cd restapi_mail`

`echo 'DATABASE_URL=postgres://<user>:<password>@<host>:<port>/<database_name>' >> .env`

Set secret key

`echo 'SECRET_KEY=<secret key>' >> .env`

`cd ..`

Create the database tables

`python manage.py makemigrations`

`python manage.py migrate`

To be able to use the admin panel:

`python manage.py createsuperuser --email admin@example.com --username admin`