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
            "first_name": "John",
            "last_name": "Doe",
            "role": "Manager",
            "status": "Active",
            "hire_date": "2024-11-14",
            "email": "john.doe@example.com",
            "phone_number": "+1234567890"
        },
        {
            "buyer_id": 2,
            "first_name": "Jane",
            "last_name": "Smith",
            "role": "Receptionist",
            "status": "Active",
            "hire_date": "2023-05-10",
            "email": "jane.smith@example.com",
            "phone_number": "+9876543210"
        }
        
GetbuyerbyId
------------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/buyer/buyers/5/``

- **Description:** Fetches details of a specific buyer using their ID.

- **Response Body:**

  .. code-block:: json

    
        {
            "buyer_id": 1,
            "first_name": "John",
            "last_name": "Doe",
            "role": "Manager",
            "status": "Active",
            "hire_date": "2024-11-14",
            "email": "john.doe@example.com",
            "phone_number": "+1234567890"
        }
  

Createbuyer
--------------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/buyer/create-buyers/``

- **Request Body:**

  .. code-block:: json

     {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone_number": "+1234567890",
            "role": "Manager",
            "status": "Active",
            "hire_date": "2024-11-14",
            "address": "123 Villa Street, Stayvillas, City, Country",
            "salary": 5000.00
        }

- **Description:** Adds a new buyer to the system.

- **Response Body:**

  .. code-block:: json

    {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "phone_number": "+1234567890",
        "role": "Manager",
        "status": "Active",
        "hire_date": "2024-11-14",
        "address": "123 Villa Street, Stayvillas, City, Country",
        "salary": 5000.00
    }





Updatebuyer
--------------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/buyer/update-buyer/{Id}/``

- **Request Body:**

  .. code-block:: json

    
        {
    "id": 5,
    "buyer_name": "Dairy",
    "buyer_description": "all types dairy buyer available",
    "org_id": null,
    "created_at": "2024-11-12T04:51:03.280121Z",
    "updated_at": "2024-11-12T04:51:03.280121Z",
    "is_active": true

        }

- **Description:** Updates information for a specific buyer.

- **Response Body:**

  .. code-block:: json

    {
        
    "id": 5,
    "buyer_name": "Dairy",
    "buyer_description": "all types dairy buyer available",
    "org_id": null,
    "created_at": "2024-11-12T04:51:03.280121Z",
    "updated_at": "2024-11-12T04:51:03.280121Z",
    "is_active": true
        
    }
    
