Category API
===========

This document describes the endpoints available for managing Categories.

Getcategory
-----------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/category/category/``

- **Description:** Retrieves a list of all Category.

- **Response Body:**

  .. code-block:: json

    {
        "status": "success",
        "data": [
            {
                 "id": 1,
        "category_name": "Smartphones",
        "category_description": "All types of smartphones.",
        "org_id": null,
        "created_at": "2024-11-11T12:51:10.626483Z",
        "updated_at": "2024-11-11T12:51:10.626483Z",
        "is_active": true
            }
        ]
    }

GetCategorybyId
------------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/category/category/5/``

- **Description:** Fetches details of a specific category using their ID.

- **Response Body:**

  .. code-block:: json

    {
        "status": "success",
        "data": [
            {
                 "id": 1,
        "category_name": "Smartphones",
        "category_description": "All types of smartphones.",
        "org_id": null,
        "created_at": "2024-11-11T12:51:10.626483Z",
        "updated_at": "2024-11-11T12:51:10.626483Z",
        "is_active": true
            }
        ]
    }

CreateCategory
--------------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/category/create-category/``

- **Request Body:**

  .. code-block:: json

    {
        {
    "category_name": "fruits",
    "category_description": "all types fresh vegetables available",
    "is_active": true
        }
    }

- **Description:** Adds a new category to the system.

- **Response Body:**

  .. code-block:: json

    {
        {
    "id": 7,
    "category_name": "fruits",
    "category_description": "all types fresh vegetables available",
    "org_id": null,
    "created_at": "2024-11-14T06:21:58.546304Z",
    "updated_at": "2024-11-14T06:21:58.547304Z",
    "is_active": true
        }
    }




UpdateCategory
--------------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/category/update-category/{Id}/``

- **Request Body:**

  .. code-block:: json

    
        {
    "id": 5,
    "category_name": "Dairy",
    "category_description": "all types dairy product available",
    "org_id": null,
    "created_at": "2024-11-12T04:51:03.280121Z",
    "updated_at": "2024-11-12T04:51:03.280121Z",
    "is_active": true

        }

- **Description:** Updates information for a specific category.

- **Response Body:**

  .. code-block:: json

    {
        {
    "id": 5,
    "category_name": "Dairy",
    "category_description": "all types dairy product available",
    "org_id": null,
    "created_at": "2024-11-12T04:51:03.280121Z",
    "updated_at": "2024-11-12T04:51:03.280121Z",
    "is_active": true
        }
    }
    
