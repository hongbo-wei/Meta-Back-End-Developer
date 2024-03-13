## This is a short guide how to test my version of Little Lemon API

### **Preface**
I created this document to make your work with my project more easy and understandable,
so if you don't find it helpful or convenient then I apologize about it. I tried my best.

### **Preparing environment**
If you use another python version then you can install `pyenv` to switch between different python versions.
First of all you need to install all dependecies for this project:  
`python3 -m pipenv install`  
Then you have to run virtual environment using the following command:  
`python3 -m pipenv shell`  
To use database properly, you have to perform migrations:  
`python3 manage.py makemigrations`  
`python3 manage.py migrate`  
That's all. You now can start testing API.

#### **Start testing**
In order to test this API only that you need is some API client
or in some cases you can use Browsable API, but it is not recommended
because you won't be able to test endpoints that need to be accessed by
concrete user token. Below you can see all necessary information that can be needed
to test this API. If something goes wrong make sure that you perform all actions as specify in this guide.
For example, make sure that you make migrations and using forward slash in the endpoint's tail.

#### **Insomnia test file**
If you want to test this API fast then you can use already created
requests importing in your Insomnia client api-test.json file. **BUT if you use this file then you must specify payload and tokens by yourself**

#### **Users creadentials**
1. username: admin  
    password: lemon666happy  
    type: Admin  
    group: Manager
2. username: manager  
    password: lemon666happy
    group: Manager
3. username: delivery_crew_1 
    password: lemon666happy
    group: Delivery crew
4. username: lewis  
    password: lemon666happy
    group: Delivery crew
5. username: delivery_crew_2
    password: lemon666happy
    group: Customer

#### **API Endpoints**
Below listed all API endpoints and their short description(expected behavior).  
**PAY ATTENTION TO THE FOLLOWING NOTES**  
**Note**: I was writting forward slash in the end of each endpoint.  
**Note**: Some aspects of this guide I didn't discribe verbose because
I assume that almost everything here is pretty clear for you.  
**Note**: You can perform only those HTTP methods that are listed below 
particular endpoint, others will be denied.

1. **/api/menu-items/**
- GET method: lists all menu items. 
    - Types of users which can call: all allowed types(even authenticated).
    - Behavior depends on user: No.
    - Status code: 200 - OK.
- POST method: creates a new menu item. 
    - Types of users which can call: Manager, Admin
    - Behavior depends on user: Yes. Nobody except Manager and Admin can perform this action. 
    - Status code: 201 - CREATED, otherwise 403 - FORBIDDEN
    - Payload: you have to specify the following values to create an item:
        - title
        - price 
        - category: category's id
        - featured: 0 or 1
2. **/api/menu-items/{menuItem}/**
- GET method: gets single menu item by its id.
    - Types of users which can call: all allowed types(even authenticated).
    - Behavior depends on user: No.
    - Status code: 200 - OK, otherwise 404 - NOT FOUND.
- PUT method: update the whole item.
    - Types of users which can call: Manager.
    - Behavior depends on user: Yes. Nobody except Manager can perform this action.
    - Status code: 200 - OK, otherwise 404 - NOT FOUND or 403 - FORBIDDEN.
- PATCH method: partial update of the item.
    - Types of users which can call: Manager.
    - Behavior depends on user: Yes. Nobody except Manager can perform this action.
    - Status code: 200 - OK, otherwise 404 - NOT FOUND or 403 - FORBIDDEN.
- DELETE method: delete single item.
    - Types of users which can call: Manager.
    - Behavior depends on user: Yes. Nobody except Manager can perform this action.
    - Status code: 204 - NO CONTENT, otherwise 404 - NOT FOUND or 403 - FORBIDDEN.
3. **/api/groups/manager/users/**
- GET method: lists all managers.
    - Types of users which can call: Manager, Admin
    - Behavior depends on user: Yes. Nobody except Manager and Admin can perform this action.
    - Status code: 200 - OK, 403 - FORBIDDEN.
- POST method: assigns the user to the Manager group.
    - Types of users which can call: Manager, Admin.
    - Behavior depends on user: Yes. Nobody except Manager and Admin can perform this action. 
    - Status code: 201 - CREATED, otherwise 403 - FORBIDDEN
    - Payload: you have to specify the following value to add the user to the group:
        - username
4. **/api/groups/manager/users/{userId}/**
- DELETE method: remove the user from the Manager group.
    - Types of users which can call: Manager.
    - Behavior depends on user: Yes. Nobody except Manager can perform this action. 
    - Status code: 200 - OK, otherwise 404 - NOT FOUND or 403 - FORBIDDEN.
5. **/api/groups/delivery-crew/users/**
- GET method: lists all delivery crew.
    - Types of users which can call: Manager.
    - Behavior depends on user: Yes. Nobody except Manager can perform this action.
    - Status code: 200 - OK, 403 - FORBIDDEN.
- POST method: assigns the user to the Delivery crew group.
    - Types of users which can call: Manager.
    - Behavior depends on user: Yes. Nobody except Manager can perform this action. 
    - Status code: 201 - CREATED, otherwise 403 - FORBIDDEN
    - Payload: you have to specify the following value to add the user to the group:
        - username
6. **/api/groups/delivery-crew/users/{userId}/**
- DELETE method: remove the user from the Delivery group.
    - Types of users which can call: Manager.
    - Behavior depends on user: Yes. Nobody except Manager can perform this action. 
    - Status code: 200 - OK, otherwise 404 - NOT FOUND or 403 - FORBIDDEN.
7. **/api/cart/menu-items/**
- GET method: lists all cart items for the current user.
    - Types of users which can call: Customer.
    - Behavior depends on user: Yes. Nobody except Customer can perform this action.
    - Status code: 200 - OK, 403 - FORBIDDEN.
- POST method: adds the menu item to the cart.
    - Types of users which can call: Customer.
    - Behavior depends on user: Yes. Nobody except Customer can perform this action. 
    - Status code: 201 - CREATED, otherwise 403 - FORBIDDEN
    - Payload: you have to specify the following values to add the menu item to the cart:
        - menuitem: menuitem's id
        - quantity
- DELETE method: deletes all menu items by the current user.
    - Types of users which can call: Customer.
    - Behavior depends on user: Yes. Nobody except Customer can perform this action. 
    - Status code: 200 - OK, otherwise 403 - FORBIDDEN.
8. **/api/orders/**
- GET method: lists orders (behavior depends on particular user).
    - Types of users which can call: Customer, Manager, Delivery crew.
    - Behavior depends on user: Yes.
        - Customer: lists all orders with order items created by this user.
        - Manager: lists all orders with order items by all users.
        - Delivery crew: lists all orders with order items assigned to this user.
    - Status code: 200 - OK, otherwise 401 - Unauthorized
- POST method: creates new order with order items that are moved from user's cart, after that all items from the cart deletes.
    - Types of users which can call: Customer.
    - Behavior depends on user: Yes. Nobody except Customer can perform this action. 
    - Status code: 201 - CREATED, otherwise 403 - FORBIDDEN
    - Payload: no payload needs.
9. **/api/orders/{orderId}/**
- GET method: gets the order created by the current user.
    - Types of users which can call: Customer.
    - Behavior depends on user: Yes. Nobody except Customer can perform this action. 
    - Status code: 200 - OK, otherwise 404 - NOT FOUND or 403 - FORBIDDEN.
- PUT method: update the order(in fact, not the whole order, but delivery_crew and status).
    - Types of users which can call: Manager.
    - Behavior depends on user: Yes. Nobody except Manager can perform this action. 
    - Status code: 200 - OK, otherwise 404 - NOT FOUND or 403 - FORBIDDEN.
- PATCH method: update the particular part of the order (depends on user).
    - Types of users which can call: Manager, Delivery crew.
    - Behavior depends on user: Yes.
        - Manager: can update any part of the order.
        - Delivery crew: can update only status.
    - Status code: 200 - OK, otherwise 404 - NOT FOUND or 403 - FORBIDDEN
- DELETE method: delete the order.
    - Types of users which can call: Manager.
    - Behavior depends on user: Yes. Nobody except Manager can perform this action.
    - Status code: 204 - NO CONTENT, otherwise 404 - NOT FOUND or 403 - FORBIDDEN.
10. **/api/categories/**
- GET method: lists all categories.
    - Types of users which can call: Customer, Admin.
    - Behavior depends on user: Yes. Nobody except Customer or Admin can perform this action. But for both behavior is the same.
    - Status code: 200 - OK, otherwise 403 - FORBIDDEN.
- POST method: create a new category:
    - Types of users which can call: Admin.
    - Behavior depends on user: Yes. Nobody except Admin can perform this action.
    - Status code: 201 - CREATED, otherwise 403 - FORBIDDEN.
11. **/api/categories/{categoryId}/**
- PUT method: update the category
    - Types of users which can call: Admin.
    - Behavior depends on user: Yes. Nobody except Admin can perform this action.
    - Status code: 200 - OK, otherwise 403 - FORBIDDEN.
- PATCH method: partial update of the category
    - Types of users which can call: Admin.
    - Behavior depends on user: Yes. Nobody except Admin can perform this action.
    - Status code: 200 - OK, otherwise 403 - FORBIDDEN.
- DELETE method: delete the category.
    - Types of users which can call: Admin.
    - Behavior depends on user: Yes. Nobody except Admin can perform this action.
    - Status code: 204 - NO CONTENT, otherwise 403 - FORBIDDEN.