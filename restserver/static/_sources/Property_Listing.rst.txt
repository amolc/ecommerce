Property_Listing API
========================

This document describes the (Create, Read, Update) operations for the `Property_Listing` model in the application.

**Property_Listing Model**


The `Property_Listing` model represents a user in the system and includes the following fields:

- `org_id` (integer): The organization ID associated with the customer.
- `email` (string): The email address of the customer.
- `password` (string): The hashed password of the customer (stored securely).
- `first_name` (string): The first name of the customer.
- `last_name` (string): The last name of the customer.
- `city` (string): The city where the customer resides.
- `mobile_number` (string): The mobile phone number of the customer.
- `property_location` (string): The location of the customer's property.
- `property_type` (string): The type of property. 
- `num_rooms` (decimal): The number of rooms in the property.
- `heard_from` (string): Where the customer heard about the service.
- `photo_website` (string): URL to the customer's property photos hosted on the web.
- `property_description` (string): A detailed description of the property.
- `is_active` (boolean): Whether the customer's profile is currently active.
- `is_featured` (boolean): Whether the customer's property is featured on the platform.
- `is_verified` (boolean): Whether the customer or their property is verified by the platform.
            
**URL**

**Local Development URL:**

- `baseurl`` = "http://localhost:7777/1/api/"

**Production URL:**

- `baseurl`` = "https://api.sunandsandapi.com/1/api/"

Property_List
=============

GetAllProperty_List
---------------------

- **Endpoint:** ``GET baseUrl/org_id/api/property_listing/get-property_list/``

- **Response Body:**

.. code-block:: json

    {
    "status": "success",
    "data": [
        {
            "id": 1,
            "org_id": 1,
            "first_name": "Vaishali",
            "last_name": "Deokar",
            "email": "johndoe@example.com",
            "mobile_no": "1234567890",
            "property_location": "123 Main St, Springfield",
            "property_type": "Villa",
            "num_rooms": 3,
            "heard_from": "Facebook",
            "photo_website": "https://example.com/property.jpg",
            "property_description": "A beautiful villa with a great view.",
            "is_active": true,
            "is_featured": true,
            "is_verified": false
        }
            ]
    }   
GetProperty_ListById
---------------------

- **Endpoint:** ``GET baseUrl/org_id/property_listing/get-property_list/{Id}/``

- **Response Body:**

.. code-block:: json

    {
    "status": "success",
    "data": {
        "id": 1,
        "org_id": 1,
        "first_name": "Vaishali",
        "last_name": "Deokar",
        "email": "johndoe@example.com",
        "mobile_no": "1234567890",
        "property_location": "123 Main St, Springfield",
        "property_type": "Villa",
        "num_rooms": 3,
        "heard_from": "Facebook",
        "photo_website": "https://example.com/property.jpg",
        "property_description": "A beautiful villa with a great view.",
        "is_active": true,
        "is_featured": true,
        "is_verified": false
            }
    }

CreateProperty_List
----------------------

- **Endpoint:** ``POST baseUrl/org_id/api/property_listing/create-property_list/``

- **Request Body:**

.. code-block:: json

    {
    "first_name": "vaishali",
    "last_name": "kadbhane",
    "email": "vaishali@example.com",
    "mobile_no": "1234567890",
    "property_location": "Lonavala",
    "property_type": "Bungalow",
    "num_rooms": 5,
    "heard_from": "Instagram",
    "photo_website": "https://example.com/property.jpg",
    "property_description": "A beautiful villa with a great view.",
    "is_active": true,
    "is_featured": true,
    "is_verified": false
    }

- **Response Body:**

.. code-block:: json

    {
    "status": "success",
    "data": {
        "id": 5,
        "org_id": 1,
        "first_name": "vaishali",
        "last_name": "kadbhane",
        "email": "vaishali@example.com",
        "mobile_no": "1234567890",
        "property_location": "Lonavala",
        "property_type": "Bungalow",
        "num_rooms": 5,
        "heard_from": "Instagram",
        "photo_website": "https://example.com/property.jpg",
        "property_description": "A beautiful villa with a great view.",
        "is_active": true,
        "is_featured": true,
        "is_verified": false
            }
    }

UpdateProperty_List
----------------------

- **Endpoint:** `POST baseUrl/org_id/property_listing/update-property_list/{1}/`

- **Request Body:**

.. code-block:: json

    {  
            "first_name": "Vaishali",
            "last_name": "Deokar",
            "email": "johndoe@example.com",
            "mobile_no": "1234567890",
            "property_location": "123 Main St, Springfield",
            "property_type": "Villa",
            "num_rooms": 3,
            "heard_from": "Facebook",
            "photo_website": "https://example.com/property.jpg",
            "property_description": "A beautiful villa with a great view.",
            "is_active": true,
            "is_featured": true,
            "is_verified": false
        
    }

- **Response Body:**

.. code-block:: json
    
    {
    "status": "success",
    "data": {
        "id": 1,
        "org_id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe@example.com",
        "mobile_no": "1234567890",
        "property_location": "123 Main St, Springfield",
        "property_type": "Villa",
        "num_rooms": 3,
        "heard_from": "Facebook",
        "photo_website": "https://example.com/property.jpg",
        "property_description": "A beautiful villa with a great view.",
        "is_active": true,
        "is_featured": true,
        "is_verified": false
        }
    }
