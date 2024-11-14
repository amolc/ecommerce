Subcategory API
==============

This document describes the endpoints available for managing Subcategories.

Getsubcategory
--------------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/subcategory/subcategory/``

- **Description:** Retrieves a list of all Subcategory.

- **Response Body:**

  .. code-block:: json

    {
    "status": "success",
    "data": [
        {
            "id": 4,
            "subcategory_name": "Mobile Accessories",
            "subcategory_description": "A variety of mobile accessories including cases, chargers, and more.",
            "org_id": null,
            "category": 2,
            "created_at": "2024-11-11T19:13:37.467492Z",
            "updated_at": "2024-11-11T19:13:37.467492Z",
            "is_active": true
        },
        {
            "id": 5,
            "subcategory_name": "Mobile Accessories",
            "subcategory_description": "A variety of mobile accessories including cases, chargers, and more.",
            "org_id": null,
            "category": 2,
            "created_at": "2024-11-12T04:08:46.184242Z",
            "updated_at": "2024-11-12T04:08:46.184242Z",
            "is_active": true
        },
    ]
    }

GetSubcategorybyId
------------------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/subcategory/subcategory/2/``

- **Description:** Fetches details of a specific Subcategory using their ID.

- **Response Body:**

  .. code-block:: json
{
    "status": "success",
    "data": [
        {
            "id": 4,
            "subcategory_name": "Mobile Accessories",
            "subcategory_description": "A variety of mobile accessories including cases, chargers, and more.",
            "org_id": null,
            "category": 2,
            "created_at": "2024-11-11T19:13:37.467492Z",
            "updated_at": "2024-11-11T19:13:37.467492Z",
            "is_active": true
        },

CreateSubcategory
--------------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/subcategory/create-subcategory/``

- **Request Body:**

  .. code-block:: json

    {
  "category_id": 2,
  "subcategory_name": "milk",
  "subcategory_description": "cow and buffelo milk available"
  
}


- **Description:** Adds a new subcategory to the system.

- **Response Body:**

  .. code-block:: json

    {
    "status": "success",
    "data": {
        "id": 12,
        "subcategory_name": "milk",
        "subcategory_description": "cow and buffelo milk available",
        "org_id": 1,
        "category": 2,
        "created_at": "2024-11-14T06:36:08.857374Z",
        "updated_at": "2024-11-14T06:36:08.857935Z",
        "is_active": true
    }
}



UpdateSubcategory
--------------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/subcategory/update-subcategory/2/``

- **Request Body:**

  .. code-block:: json

    
    {
        "status": "success",
        "data": [
            {
                "id": 4,
                "subcategory_name": "Mobile Accessories",
                "subcategory_description": "A variety of mobile accessories including cases, chargers, and more.",
                "org_id": null,
                "category": 2,
                "created_at": "2024-11-11T19:13:37.467492Z",
                "updated_at": "2024-11-11T19:13:37.467492Z",
                "is_active": true
            },

- **Description:** Updates information for a specific Subcategory.

- **Response Body:**

  .. code-block:: json

    {
        "status": "success",
        "data": [
            {
                "id": 4,
                "subcategory_name": "Mobile",
                "subcategory_description": "A variety of mobile accessories including cases, chargers, and more.",
                "org_id": null,
                "category": 2,
                "created_at": "2024-11-11T19:13:37.467492Z",
                "updated_at": "2024-11-11T19:13:37.467492Z",
                "is_active": true
            },
        
