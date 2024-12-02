Customers API
============

This document describes the endpoints available for managing Categories.

GetCustomers
-----------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/product/products/``

- **Description:** Retrieves a list of all Customers.

- **Response Body:**

  .. code-block:: json

    {
    "status": "success",
    "data": [
        {
            "id": 1,
            "product_name": "Example Product",
            "product_description": "This is a description of the example product.",
            "price": "19.99",
            "stock_quantity": 100,
            "org_id": 1,
            "created_at": "2024-11-12T06:34:16.731791Z",
            "updated_at": "2024-11-12T06:34:16.731791Z",
            "is_active": true,
            "category": 2,
            "subcategory": null
        },
        {
            "id": 5,
            "product_name": "potato",
            "product_description": "fresh potato.",
            "price": "39.00",
            "stock_quantity": 100,
            "org_id": 1,
            "created_at": "2024-11-12T08:47:54.533655Z",
            "updated_at": "2024-11-12T08:47:54.533655Z",
            "is_active": true,
            "category": 2,
            "subcategory": 4
        },
GetCustomersbyId
------------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/product/products/5/``

- **Description:** Fetches details of a specific Customers using their ID.

- **Response Body:**

  .. code-block:: json

   {
    "status": "success",
    "data": {
        "id": 5,
        "product_name": "potato",
        "product_description": "fresh potato.",
        "price": "39.00",
        "stock_quantity": 100,
        "org_id": 1,
        "created_at": "2024-11-12T08:47:54.533655Z",
        "updated_at": "2024-11-12T08:47:54.533655Z",
        "is_active": true,
        "category": 2,
        "subcategory": 4
    }
}


CreateCustomers
---------------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/customer/create-customer/``

- **Request Body:**

  .. code-block:: json

    {
  "org_id": 1,
  "email": "vaishaliDeokar@example.com",
  "password": "admi123",
  "first_name": "Jay",
  "last_name": "Doe",
  "city": "New York",
  "mobile_number": "1234567890",
  "is_active": true,
  "is_super_admin": false,
  "is_admin": false,
  "is_customer": true
}


- **Description:** Adds a new Customers to the system.

- **Response Body:**

  .. code-block:: json

   {
    "id": 9,
    "last_login": null,
    "org_id": 1,
    "email": "vaishaliDeokar@example.com",
    "first_name": "Jay",
    "last_name": "Doe",
    "city": "New York",
    "mobile_number": "1234567890",
    "is_active": true,
    "is_super_admin": false,
    "is_admin": false,
    "is_customer": true,
    "user_id": 9
    }




