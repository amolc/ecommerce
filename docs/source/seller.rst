Seller API
===========

This document describes the endpoints available for managing seller.

Getseller
-----------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/seller/sellers/``

- **Description:** Retrieves a list of all seller.

- **Response Body:**

  .. code-block:: json

    
        {
            "seller_id": 1,
            "first_name": "John",
            "last_name": "Doe",
            "role": "Manager",
            "status": "Active",
            "hire_date": "2024-11-14",
            "email": "john.doe@example.com",
            "phone_number": "+1234567890"
        },
        {
            "seller_id": 2,
            "first_name": "Jane",
            "last_name": "Smith",
            "role": "Receptionist",
            "status": "Active",
            "hire_date": "2023-05-10",
            "email": "jane.smith@example.com",
            "phone_number": "+9876543210"
        }
        
GetsellerbyId
------------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/seller/sellers/5/``

- **Description:** Fetches details of a specific seller using their ID.

- **Response Body:**

  .. code-block:: json

    
        {
            "seller_id": 1,
            "first_name": "John",
            "last_name": "Doe",
            "role": "Manager",
            "status": "Active",
            "hire_date": "2024-11-14",
            "email": "john.doe@example.com",
            "phone_number": "+1234567890"
        }
  

Createseller
--------------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/seller/create-sellers/``

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

- **Description:** Adds a new seller to the system.

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





Updateseller
--------------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/seller/update-seller/{Id}/``

- **Request Body:**

  .. code-block:: json

    
        {
    "id": 5,
    "seller_name": "Dairy",
    "seller_description": "all types dairy seller available",
    "org_id": null,
    "created_at": "2024-11-12T04:51:03.280121Z",
    "updated_at": "2024-11-12T04:51:03.280121Z",
    "is_active": true

        }

- **Description:** Updates information for a specific seller.

- **Response Body:**

  .. code-block:: json

    {
        
    "id": 5,
    "seller_name": "Dairy",
    "seller_description": "all types dairy seller available",
    "org_id": null,
    "created_at": "2024-11-12T04:51:03.280121Z",
    "updated_at": "2024-11-12T04:51:03.280121Z",
    "is_active": true
        
    }
    
