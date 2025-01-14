delivery API
===========

This document describes the endpoints available for managing delivery.

Getdelivery
-----------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/delivery/deliverys/``

- **Description:** Retrieves a list of all delivery.

- **Response Body:**

  .. code-block:: json

    
        {
            "delivery_id": 1,
            "first_name": "John",
            "last_name": "Doe",
            "role": "Manager",
            "status": "Active",
            "hire_date": "2024-11-14",
            "email": "john.doe@example.com",
            "phone_number": "+1234567890"
        },
        {
            "delivery_id": 2,
            "first_name": "Jane",
            "last_name": "Smith",
            "role": "Receptionist",
            "status": "Active",
            "hire_date": "2023-05-10",
            "email": "jane.smith@example.com",
            "phone_number": "+9876543210"
        }
        
GetdeliverybyId
------------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/delivery/deliverys/5/``

- **Description:** Fetches details of a specific delivery using their ID.

- **Response Body:**

  .. code-block:: json

    
        {
            "delivery_id": 1,
            "first_name": "John",
            "last_name": "Doe",
            "role": "Manager",
            "status": "Active",
            "hire_date": "2024-11-14",
            "email": "john.doe@example.com",
            "phone_number": "+1234567890"
        }
  

Createdelivery
--------------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/delivery/create-deliverys/``

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

- **Description:** Adds a new delivery to the system.

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





Updatedelivery
--------------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/delivery/update-delivery/{Id}/``

- **Request Body:**

  .. code-block:: json

    
        {
    "id": 5,
    "delivery_name": "Dairy",
    "delivery_description": "all types dairy delivery available",
    "org_id": null,
    "created_at": "2024-11-12T04:51:03.280121Z",
    "updated_at": "2024-11-12T04:51:03.280121Z",
    "is_active": true

        }

- **Description:** Updates information for a specific delivery.

- **Response Body:**

  .. code-block:: json

    {
        
    "id": 5,
    "delivery_name": "Dairy",
    "delivery_description": "all types dairy delivery available",
    "org_id": null,
    "created_at": "2024-11-12T04:51:03.280121Z",
    "updated_at": "2024-11-12T04:51:03.280121Z",
    "is_active": true
        
    }
    
