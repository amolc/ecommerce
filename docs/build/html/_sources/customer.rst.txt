Customer API
===============

This document describes the (Create, Read, Login) operations for the `Customer` model in the application.

**Customer Model**


The `Customer` model represents a user in the system and includes the following fields:

- `org_id` (integer): The organization ID associated with the customer.
- `email` (string): The email address of the customer.
- `password` (string): The hashed password of the customer (stored securely).
- `first_name` (string): The first name of the customer.
- `last_name` (string): The last name of the customer.
- `city` (string): The city where the customer resides.
- `mobile_number` (string): The mobile phone number of the customer.
- `is_active` (boolean): Indicates whether the customer is active.
- `is_super_admin` (boolean): Indicates whether the customer has super admin privileges.
- `is_admin` (boolean): Indicates whether the customer has admin privileges.
- `is_customer` (boolean): Indicates whether the user is marked as a customer.
- `Token`(string):The authentication token used to validate the customer's session.
- `Status`(string):The current status of the customer.
- `displayName`(string): The display name of the customer, typically used for showing in user interfaces.
        
**URL**


**Local Development URL:**

- `baseurl`` = "http://localhost:8888/1/api/"

**Production URL:**

- `baseurl`` = "https://api.sunandsandapi.com/1/api/"

.. Customer
.. ========

GetAllCustomer
---------------

- **Endpoint:** ``GET baseUrl/org_id/api/customer/get-customer/``

- **Response Body:**

.. code-block:: json
    
    {
    "status": "success",
    "data": [
        {
            "id": 1,
            "last_login": null,
            "org_id": 3,
            "email": "example@example.com",
            "password": "pbkdf2_sha256$870000$u6iZn1Yfho8aca2ORYPM51$9gT/uIUu74ThrP/sOhOZXIAlAEvSnljEO3OhXQ4ZoBY=",
            "first_name": "John",
            "last_name": "Doe",
            "city": "New York",
            "mobile_number": "+1234567890",
            "is_active": true,
            "is_super_admin": false,
            "is_admin": false,
            "is_customer": true
        }
            ]
    }

GetCustomerById
----------------

- **Endpoint:** ``GET baseUrl/org_id/api/customer/get-customer/{Id}/``

- **Response Body:**

.. code-block:: json
    
    {
    "status": "success",
    "data": [
        {
            "id": 1,
            "last_login": null,
            "org_id": 3,
            "email": "example@example.com",
            "password": "pbkdf2_sha256$870000$u6iZn1Yfho8aca2ORYPM51$9gT/uIUu74ThrP/sOhOZXIAlAEvSnljEO3OhXQ4ZoBY=",
            "first_name": "John",
            "last_name": "Doe",
            "city": "New York",
            "mobile_number": "+1234567890",
            "is_active": true,
            "is_super_admin": false,
            "is_admin": false,
            "is_customer": true
        }
            ]
    }

CreateCustomer
-----------------

- **Endpoint:** ``POST baseUrl/org_id/api/customer/create-customer/``

- **Request Body:**

.. code-block:: json
    
    {
  "org_id": 1,
  "email": "example@example.com",
  "password": "password",
  "first_name": "John",
  "last_name": "Doe",
  "city": "New York",
  "mobile_number": "+1234567890",
  "is_active": true,
  "is_super_admin": false,
  "is_admin": false,
  "is_customer": true
    }

- **Response Body:**

.. code-block:: json
    
    {
    "id": 1,
    "last_login": null,
    "org_id": 3,
    "email": "example@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "city": "New York",
    "mobile_number": "+1234567890",
    "is_active": true,
    "is_super_admin": false,
    "is_admin": false,
    "is_customer": true
    }

LoginCustomer
-------------

- **Endpoint:** ``POST baseUrl/org_id/api/customer/login-customer/``

- **Request Body:**

.. code-block:: json
    
    {
    "email": "example@example.com",
    "password": "password"
    }

- **Response Body:**

.. code-block:: json
    
    {
    "status": "success",
    "data": {
        "status": 200,
        "user_id": 1,
        "is_super_admin": false,
        "is_admin": false,
        "is_customer": true,
        "displayName": "John",
        "emailId": "example@example.com",
        "message": "Logged-in Successfully",
        "Token": "612e9a50ad61e6c2c6b5f9b8cbc9dd773981958c82cf276156904920c79d2664"
            }
    }