# REST API for sending emails

### To run locally
Clone the repository

`$ git clone https://github.com/Kalarebka/restapi-mail.git`

`$ cd restapi-mail`

Create a virtual environment

`$ python3.10 -m venv env`

`$ source env/bin/activate`

Install dependencies

`$ pip install -r requirements.txt`

Create a database and an .env file with the path to the database

`$ createdb <database_name>`

`$ cd restapi_mail`

`$ echo 'DATABASE_URL=postgres://<user>:<password>@<host>:<port>/<database_name>' >> .env`

Set secret key

`$ echo 'SECRET_KEY=<secret key>' >> .env`

`$ cd ..`

Create the database tables

`$ python manage.py makemigrations`

`$ python manage.py migrate`

To be able to use the admin panel:

`$ python manage.py createsuperuser --email admin@example.com --username admin`

Install and setup RabbitMQ message broker for Celery

`$ sudo apt-get install rabbitmq-server`

`$ sudo rabbitmqctl add_user myuser mypassword`

`$ sudo rabbitmqctl add_vhost myvhost`

`$ sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"`

`$ echo "BROKER_URL='amqp://myuser:mypassword@localhost:5672/myvhost'" >> .env`

Run Celery worker
`$ celery -A restapi_mail worker -l INFO`

Run Django server
`$ python manage.py runserver`