Commands to use: 

pipenv shell
pipenv install django

#creating a project
django-admin startproject lilttlelemon

#creating an app
python manage.py startapp restaurant

#cd to folder containing the manage.py file
python manage.py runserver

#install client
pipenv install mysqlclient

IN DB:
create database littlelemon;


python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

username:admin
email: admin@little.lemon
password:lemon@1234!

User :
username: Jessica
password: Jess12345!

pipenv install djangorestframework

pipenv install djoser

python manage.py test

In browser:
http://127.0.0.1:8000/restaurant/menu/1 -> To view the details of single item

http://127.0.0.1:8000/restaurant/booking/tables/ -> To view the booking list

In Insomnia: 

POST: http://127.0.0.1:8000/restaurant/api-token-auth/
authentication required: (Can either provide user's credentials or admin's)

#To get the details of all menu
GET: http://127.0.0.1:8000/restaurant/menu/1 

#To add menu item
POST: http://127.0.0.1:8000/restaurant/menu/ 
and give details in JSON format in the body

#To get the details of menu item 1
GET: http://127.0.0.1:8000/restaurant/menu/1 

#To get the details of bookings
GET: http://127.0.0.1:8000/restaurant/booking/tables/

#To create tokens for the user
http://127.0.0.1:8000/auth/token/login/

