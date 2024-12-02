Buyer API
===========

This document describes the endpoints available for managing buyer.

Getbuyer
--------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/buyer/buyers/``

- **Description:** Retrieves a list of all buyer.

- **Response Body:**

  .. code-block:: json

    
     {
    "buyer_id": 1,
    "first_name": "Alice",
    "last_name": "Smith",
    "email": "alice.smith@example.com",
    "phone_number": "+1234567890",
    "address": "456 Commerce Street, Cityville, Country",
    "registration_date": "2024-11-14T10:00:00Z",
    "is_active": true
    }
            
        
GetbuyerbyId
------------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/buyer/buyers/5/``

- **Description:** Fetches details of a specific buyer using their ID.

- **Response Body:**

  .. code-block:: json

    
    {
    "buyer_id": 1,
    "first_name": "Alice",
    "last_name": "Smith",
    "email": "alice.smith@example.com",
    "phone_number": "+1234567890",
    "address": "456 Commerce Street, Cityville, Country",
    "registration_date": "2024-11-14T10:00:00Z",
    "is_active": true
    }
  

Createbuyer
--------------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/buyer/create-buyers/``

- **Request Body:**

  .. code-block:: json

    {
    "first_name": "Alice",
    "last_name": "Smith",
    "email": "alice.smith@example.com",
    "phone_number": "+1234567890",
    "address": "456 Commerce Street, Cityville, Country",
    "is_active": true
    }

- **Description:** Adds a new buyer to the system.

- **Response Body:**

  .. code-block:: json

        {
    "buyer_id": 1,
    "first_name": "Alice",
    "last_name": "Smith",
    "email": "alice.smith@example.com",
    "phone_number": "+1234567890",
    "address": "456 Commerce Street, Cityville, Country",
    "registration_date": "2024-11-14T10:00:00Z",
    "is_active": true
    }





Updatebuyer
--------------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/buyer/update-buyer/{Id}/``

- **Request Body:**

  .. code-block:: json

        
     {
    "buyer_id": 1,
    "first_name": "Alice",
    "last_name": "Smith",
    "email": "alice.smith@example.com",
    "phone_number": "+1234567890",
    "address": "456 Commerce Street, Cityville, Country",
    "registration_date": "2024-11-14T10:00:00Z",
    "is_active": true
    }

- **Description:** Updates information for a specific buyer.

- **Response Body:**

  .. code-block:: json

        {
    "buyer_id": 1,
    "first_name": "Ali",
    "last_name": "Smith",
    "email": "ali.smith@example.com",
    "phone_number": "+1234567890",
    "address": "456 Commerce Street, Cityville, Country",
    "registration_date": "2024-11-14T10:00:00Z",
    "is_active": true
    }
