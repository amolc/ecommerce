Property_manager API
====================

This document describes the (Create, Read, Update) operations for the `Property_manager` model in the application.

**Property_manager Model**

The `Property_manager` model represents a user in the system and includes the following fields:

- `org_id` (integer): The organization ID associated with the customer.
- `manager_name` (string): The name of the property manager
- `manager_email` (string):The email address of the property manager
- `manager_phone` (string): The phone number of the property manager.
- `availability_status` (string): The current availability status of the property manager
- `date_of_hire` (date): The date the property manager was hired
- `total_properties_managed` (string): The total number of properties the property manager is responsible for.
- `address` (string):The address of the property manager

**URL**

**Local Development URL:**

- `baseurl`` = "http://localhost:7777/1/api/"

**Production URL:**

- `baseurl`` = "https://api.sunandsandapi.com/1/api/"

.. Property_manager
.. ================

GetProperty_manager 
-------------------

- **Endpoint:** ``GET baseUrl/org_id/api/property_manager/get-property_manager/``

- **Response Body:**

.. code-block:: json

    {
    "status": "success",
    "data": [
        {
            "id": 3,
            "org_id": 1,
            "manager_name": "Onkar",
            "manager_email": "okdaw@gmail.com",
            "manager_phone": "+1237356789",
            "availability_status": true,
            "date_of_hire": "2024-09-21T12:34:56Z",
            "total_properties_managed": 4,
            "address": "123 Main St, Anytown, USA"
        }
            ]
    }

GetProperty_managerById
-----------------------

- **Endpoint:** ``GET /{org_id}/api/property_manager/get-property_manager/{Id}/``

- **Response Body:**

.. code-block:: json

    {
    "status": "success",
    "data": {
        "id": 3,
        "org_id": 1,
        "manager_name": "Onkar",
        "manager_email": "okdaw@gmail.com",
        "manager_phone": "+1237356789",
        "availability_status": true,
        "date_of_hire": "2024-09-21T12:34:56Z",
        "total_properties_managed": 4,
        "address": "123 Main St, Anytown, USA"
            }
     }

CreateProperty_manager
----------------------

- **Endpoint:** ``POST baseUrl/org_id/api/property_manager/create-property_manager/``

- **Request Body:**

.. code-block:: json

    {
  "manager_name": "vaishalikad",
  "manager_email": "vaishali22@example.com",
  "manager_phone": "+1245676789",
  "availability_status": true,
  "date_of_hire": "2023-09-15T12:34:56Z",
  "total_properties_managed": 10,
  "address": "1234 Elm St, Springfield"
    }


- **Response Body:**

.. code-block:: json

    {
    "status": "success",
    "data": {
        "id": 7,
        "org_id": 1,
        "manager_name": "vaishalikad",
        "manager_email": "vaishali22@example.com",
        "manager_phone": "+1245676789",
        "availability_status": true,
        "date_of_hire": "2023-09-15T12:34:56Z",
        "total_properties_managed": 10,
        "address": "1234 Elm St, Springfield"
    }
}

UpdateProperty_manager
---------------------

- **Endpoint:** ``Patch baseUrl/org_id/api/property_manager/update-property_manager/{Id}/``
- **Request Body:**

.. code-block:: json

    {
  "manager_name": "vaishali",
  "manager_email": "kadbhane@example.com",
  "manager_phone": "+15673456789",
  "availability_status": true,
  "date_of_hire": "2023-09-15T12:34:56Z",
  "total_properties_managed": 10,
  "address": "1234 Elm St, Springfield"
    }


- **Response Body:**

.. code-block:: json

    {
    "status": "success",
    "data": {
        "id": 7,
        "org_id": 1,
        "manager_name": "vaishali",
        "manager_email": "kadbhane@example.com",
        "manager_phone": "+15673456789",
        "availability_status": true,
        "date_of_hire": "2023-09-15T12:34:56Z",
        "total_properties_managed": 10,
        "address": "1234 Elm St, Springfield"
            }
    }

[Link Text](file:///C:/Users/vaishali%20mayuresh/OneDrive/Desktop/Project2024/stayvillas-api/docs/build/html/Destination.html)
