Property API
============

This document outlines the CRUD operations for the `Property` model in the application.

**Property Model**


The `Property` model represents a user in the system and includes the following fields:


- `org_id`` (Positive Integer): The organization ID associated with the property.
- `property_name` (CharField): The name of the property. Maximum length of 200 characters.
- `property_key_name` (CharField): The key name of the property. Maximum length of 200 characters. This field is optional (nullable).
- `is_active` (BooleanField): Indicates whether the property is active. Defaults to `True`.
- `city` (CharField): The city where the property is located. Maximum length of 200 characters.
- `state` (CharField): The state where the property is located. Maximum length of 200 characters.
- `cost_per_night` (DecimalField): The cost per night for the property. This field has a maximum of 10 digits, with 2 decimal places. It is optional (nullable).
- `created_date` (DateTimeField): The timestamp indicating when the property was created. This is automatically set when the property is created.
- `created_by` (IntegerField): The ID of the user who created the property. Defaults to `0`.
- `updated_date` (DateTimeField): The timestamp indicating when the property was last updated. This field is optional (nullable).
- `updated_by`` (IntegerField): The ID of the user who last updated the property. Defaults to `0`.

**URL**

**Local Development URL:**

- `baseurl`` = "http://localhost:8888/1/api/"

**Production URL:**

- `baseurl`` = "https://api.sunandsandapi.com/1/api/"

.. Property
.. ========

GetAllProperties
----------------

- **Endpoint:** ``GET baseUrl/{org_id}/api/property/get-property/``

- **Description:**
Fetches a list of all properties associated with the given organization.

- **Response Body:**

.. code-block:: json

    {
    "status": "success",
    "data": [
        {
            "id": 1,
            "org_id": 3,
            "property_name": "Luxury Beach Villa",
            "property_key_name": "luxury_beach_villa",
            "is_active": true,
            "city": "Miami",
            "state": "Florida",
            "cost_per_night": "350.00",
            "created_date": "2024-09-13T03:50:06.642820Z",
            "created_by": 0,
            "updated_date": null,
            "updated_by": 0
        }
            ]
    }

GetById property

- **Endpoint:** `GET baseUrl/{org_id}/api/property/get-property/?id=1/`

- **Response Body:**

.. code-block:: json

    {
    "status": "success",
    "data": [
        {
            "id": 1,
            "org_id": 3,
            "property_name": "Luxury Beach Villa",
            "property_key_name": "luxury_beach_villa",
            "is_active": true,
            "city": "Miami",
            "state": "Florida",
            "cost_per_night": "350.00",
            "created_date": "2024-09-13T03:50:06.642820Z",
            "created_by": 0,
            "updated_date": null,
            "updated_by": 0
        }
            ]
    }

Create a property
-----------------

- **Endpoint:** ``POST baseUrl/{org_id}/api/property/create-property/``

- **Request Body:**

.. code-block:: json
    
    {
  "property_name": "Luxury Beach Villa",
  "property_key_name": "luxury_beach_villa",
  "is_active": true,
  "city": "Miami",
  "state": "Florida",
  "cost_per_night": 350.00
    }

- **Response Body:**

.. code-block:: json

    {
    "status": "success",
    "data": {
        "id": 1,
        "org_id": 3,
        "property_name": "Luxury Beach Villa",
        "property_key_name": "luxury_beach_villa",
        "is_active": true,
        "city": "Miami",
        "state": "Florida",
        "cost_per_night": "350.00",
        "created_date": "2024-09-13T03:50:06.642820Z",
        "created_by": 0,
        "updated_date": null,
        "updated_by": 0
            }
    }

Update a Property
-----------------

- **Endpoint:** `POST baseUrl/org_id/api/customer/create-customer/`

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
