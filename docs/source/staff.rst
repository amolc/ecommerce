Staff API
===========

This document describes the endpoints available for managing staff.

Getstaff
-----------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/staff/staffs/``

- **Description:** Retrieves a list of all staff.

- **Response Body:**

  .. code-block:: json

    
        {
            "staff_id": 1,
            "first_name": "John",
            "last_name": "Doe",
            "role": "Manager",
            "status": "Active",
            "hire_date": "2024-11-14",
            "email": "john.doe@example.com",
            "phone_number": "+1234567890"
        },
        {
            "staff_id": 2,
            "first_name": "Jane",
            "last_name": "Smith",
            "role": "Receptionist",
            "status": "Active",
            "hire_date": "2023-05-10",
            "email": "jane.smith@example.com",
            "phone_number": "+9876543210"
        }
        
GetstaffbyId
------------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/staff/staffs/5/``

- **Description:** Fetches details of a specific staff using their ID.

- **Response Body:**

  .. code-block:: json

    
        {
            "staff_id": 1,
            "first_name": "John",
            "last_name": "Doe",
            "role": "Manager",
            "status": "Active",
            "hire_date": "2024-11-14",
            "email": "john.doe@example.com",
            "phone_number": "+1234567890"
        }
  

Createstaff
--------------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/staff/create-staffs/``

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

- **Description:** Adds a new staff to the system.

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





Updatestaff
--------------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/staff/update-staff/{Id}/``

- **Request Body:**

  .. code-block:: json

    
        {
    "id": 5,
    "staff_name": "Dairy",
    "staff_description": "all types dairy staff available",
    "org_id": null,
    "created_at": "2024-11-12T04:51:03.280121Z",
    "updated_at": "2024-11-12T04:51:03.280121Z",
    "is_active": true

        }

- **Description:** Updates information for a specific staff.

- **Response Body:**

  .. code-block:: json

    {
        
    "id": 5,
    "staff_name": "Dairy",
    "staff_description": "all types dairy staff available",
    "org_id": null,
    "created_at": "2024-11-12T04:51:03.280121Z",
    "updated_at": "2024-11-12T04:51:03.280121Z",
    "is_active": true
        
    }
    
