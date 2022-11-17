# E-SHOP REST API
---
# Getting started
---
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
# Prerequisites
This is a project written using Python, Django and Django Rest Framework
1. Clone the repository
```
https://github.com/alikeev-amantur/eshop
```
2. Create the virtual enviroment
 ```
pipenv shell
```
3. Install the requirements
```
pipenv lock --requirements
```
4. Create a new PostgreSQL database

In your terminal:
```
psql postgres
CREATE DATABASE databasename
\c databasename
```
8. Create a new superuser
```
python manage.py createsuperuser
```
9. Run the server
```
python manage.py runserver
```
# Built With

> ### `Django` - The framework used
> ### `Django Rest Framework` - The toolkit used to build API

# Postman Collections

### [Collections](https://www.postman.com/alikeev/workspace/shop/documentation/21365813-e1719250-cfed-4318-8d9f-c596b2deb7ef)

# Deployed to Heroku

### [Heroku](https://bruhshop.herokuapp.com/)