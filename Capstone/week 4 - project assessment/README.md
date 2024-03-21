# [Meta Back-End Developer Professional Certificate](https://www.coursera.org/professional-certificates/meta-back-end-developer)

## [Back-end developer capstone project](https://www.coursera.org/learn/back-end-developer-capstone?specialization=meta-back-end-developer) -> LittleLemon (Full-Stack Web Application)

### How to start the application
Please run the following commands **in sequence**
```
# activate virtual environment
pipenv shell

# install all dependencies from Pipfile.lock
pipenv install

# Creates migration files based on changes to the models.
python manage.py makemigrations

# Applies pending migrations to the database.
python manage.py migrate

```

**Start the server**
```
python manage.py runserver
```

#### Endpoints

- LittleLemon Project

    - Restaurant App

        - HOME PAGE
            
            http://127.0.0.1:8000/restaurant

        - Restaurant's Menu
            
            http://127.0.0.1:8000/restaurant/menu 

        - Signle item in Menu
            
            http://127.0.0.1:8000/restaurant/menu/pk=id (change id to the actual number of a primary key, such as 1)

        - Booking Tables
        
            http://127.0.0.1:8000/restaurant/booking

        - API Booking
            
            http://127.0.0.1:8000/direct/booking

    - Authentication and Authorization
    
        - Administration Panel
            
            http://127.0.0.1:8000/admin

        - API Token Generator
            
            http://127.0.0.1:8000/restaurant/api-token-auth

        - User list
            
            http://127.0.0.1:8000/auth/users

    - API:
        - http://127.0.0.1:8000/api
        - http://127.0.0.1:8000/api/api-auth
        - http://127.0.0.1:8000/api/menu
        - http://127.0.0.1:8000/api/menu/pk=id (change id to the actual number of a primary key, such as 1)
        - http://127.0.0.1:8000/api/menu-items
        - http://127.0.0.1:8000/api/menu-items/pk=id (change id to the actual number of a primary key, such as 1)
        - http://127.0.0.1:8000/api/message
        - http://127.0.0.1:8000/api/api-token-auth
        - http://127.0.0.1:8000/api/bookings
        - http://127.0.0.1:8000/api/categories
        - http://127.0.0.1:8000/api/bookings
        - http://127.0.0.1:8000/api/categories
        - http://127.0.0.1:8000/api/cart/menu-items
        - http://127.0.0.1:8000/api/orders
        - http://127.0.0.1:8000/api/orders/pk=id (change id to the actual number of a primary key, such as 1)
        - http://127.0.0.1:8000/api/groups/manager/users
        - http://127.0.0.1:8000/api/groups/delivery-crew/users

##### Superuser:
```
# create superuser to log in the adminitration panel
python manage.py createsuperuser --username=admin --email=admin@littlelemon.com
# password: adminlemon@123
```

- username: admin
- password: adminlemon@123
- email: admin@littlelemon.com

##### Create new user
```
CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'testlemon@123';
CREATE USER 'joe'@'localhost' IDENTIFIED BY 'joelemon@123';
```

###### Test
```
python manage.py test
```