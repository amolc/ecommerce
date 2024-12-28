Invester API
============

This document describes the (Create, Read, Update) operations for the `Invester` model in the application.

**Invester Model**


The `Invester` model represents a user in the system and includes the following fields:

- `org_id` (integer): The organization ID associated with the customer.
- `email` (string): The email address of the customer.
- `password` (string): The hashed password of the customer (stored securely).
- `first_name` (string): The first name of the customer.
- `last_name` (string): The last name of the customer.
- `city` (string): The city where the customer resides.
- `mobile_number` (string): The mobile phone number of the customer.
- `investment_amount` (decimal) Defined as a decimal to allow for monetary values.
- `investment_date` (date) Specified as a date type to capture the date of the investment.
- `is_active` (boolean): Indicates whether the customer is active.
- `is_super_admin` (boolean): Indicates whether the customer has super admin privileges.
- `is_admin` (boolean): Indicates whether the customer has admin privileges.
- `is_investor` (boolean): Indicates whether the user is marked as a customer.

**URL**

**Local Development URL:**

- `baseurl`` = "http://localhost:7777/1/api/"

**Production URL:**

- `baseurl`` = "https://api.sunandsandapi.com/1/api/"

.. Invester


GetAllInvester
---------------

- **Endpoint:** ``GET baseUrl/org_id/api/investor/get-investor/``

- **Response Body:**

.. code-block:: json

    {
    "status": "success",
    "data": [
        {
            "id": 2,
            "last_login": null,
            "org_id": 1,
            "email": "lkrushana@gmail.com",
            "password": "pbkdf2_sha256$870000$Lmn4XMlMs3iSmMvHlxfIKg$Xm1MHYkVyg7D/kUDJXmLdkB6m3DF1YX3iKYenFEy8E0=",
            "first_name": "John",
            "last_name": "Doe",
            "city": "New York",
            "mobile_number": "+1234567890",
            "investment_amount": "10000.50",
            "investment_date": "2023-09-14",
            "is_active": true,
            "is_super_admin": false,
            "is_admin": false,
            "is_investor": true
        }
            ]
    }

GetInvesterById
----------------

- **Endpoint:** ``GET baseUrl/org_id/api/investor/get-investor/Id/``

- **Response Body:**

.. code-block:: json

    {
    "status": "success",
    "data": [
        {
            "id": 2,
            "last_login": null,
            "org_id": 1,
            "email": "lkrushana@gmail.com",
            "password": "pbkdf2_sha256$870000$Lmn4XMlMs3iSmMvHlxfIKg$Xm1MHYkVyg7D/kUDJXmLdkB6m3DF1YX3iKYenFEy8E0=",
            "first_name": "John",
            "last_name": "Doe",
            "city": "New York",
            "mobile_number": "+1234567890",
            "investment_amount": "10000.50",
            "investment_date": "2023-09-14",
            "is_active": true,
            "is_super_admin": false,
            "is_admin": false,
            "is_investor": true
        }
            ]
    }

CreateInvester
-----------------

- **Endpoint:** ``POST baseUrl/org_id/api/investor/create-investor/``

- **Request Body:**

.. code-block:: json

    {
  "email": "admin@gmail.com",
  "password": "admin@123",
  "first_name": "admin",
  "last_name": "admin",
  "city": "pune",
  "mobile_number": "+1234567890",
  "investment_amount": 10000.50
    }

- **Response Body:**

.. code-block:: json

    {
    "status": "success",
    "data": 
        {
        "id": 15,
        "last_login": null,
        "org_id": 1,
        "email": "admin@gmail.com",
        "password": "admin@123",
        "first_name": "admin",
        "last_name": "admin",
        "city": "pune",
        "mobile_number": "+1234567890",
        "investment_amount": "10000.50",
        "investment_date": null,
        "is_active": true,
        "is_super_admin": false,
        "is_admin": false,
        "is_investor": true
        }
    }

.. ### Login a Invester

.. **Endpoint:** `POST baseUrl/org_id/api/investor/login-investor/`

.. **Request Body:**

.. .. code-block:: json
.. {
..     "email": "example@example.com",
..     "password": "password"
.. }

.. **Response Body:**

.. '''json
.. {
   
.. }
.. }
UpdateInvester
------------------

- **Endpoint:** ``POST baseUrl/org_id/api/investor/update-investor/{Id}/``

- **Request Body:**

.. code-block:: json

    {
  "email": "lkrushanas@gmail.com",
  "password": "password",
  "first_name": "krishna",
  "last_name": "Doe",
  "city": "New York",
  "mobile_number": "+1234567890",
  "investment_amount": 10000.50,
  "investment_date": "2023-09-14",
  "is_investor": true
    }

- **Response Body:**

.. code-block:: json

    {
    "status": "success",
    "data": 
        {
        "id": 12,
        "last_login": null,
        "org_id": 1,
        "email": "lkrushanas@gmail.com",
        "password": "password",
        "first_name": "krishna",
        "last_name": "Doe",
        "city": "New York",
        "mobile_number": "+1234567890",
        "investment_amount": "10000.50",
        "investment_date": "2023-09-14",
        "is_active": true,
        "is_super_admin": false,
        "is_admin": false,
        "is_investor": true
        }
    }