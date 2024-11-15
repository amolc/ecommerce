Product API
===========

This document describes the endpoints available for managing Categories.

GetProduct
-----------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/product/products/``

- **Description:** Retrieves a list of all Product.

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

GetProductbyId
------------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/product/products/5/``

- **Description:** Fetches details of a specific Product using their ID.

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

CreateProduct
--------------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/product/create-products/``

- **Request Body:**

  .. code-block:: json

    {
    "product_name": "Sample Product",
    "product_description": "This is a sample product description.",
    "price": 99.99,
    "stock_quantity": 100,
    "category": 2,
    "subcategory": 5,
    "is_active": true
    }

- **Description:** Adds a new Product to the system.

- **Response Body:**

  .. code-block:: json

    {
    "status": "success",
    "data": {
        "id": 9,
        "product_name": "Sample Product",
        "product_description": "This is a sample product description.",
        "price": "99.99",
        "stock_quantity": 100,
        "org_id": 10,
        "created_at": "2024-11-14T07:03:12.926793Z",
        "updated_at": "2024-11-14T07:03:12.926793Z",
        "is_active": true,
        "category": 2,
        "subcategory": 5
        }
    }




UpdateProduct
--------------

- **Endpoint:** ``http://0.0.0.0:9999/1/api/Product/update-Product/{Id}/``

- **Request Body:**

  .. code-block:: json

    
        {
        
        "product_name": "Example product ",
        "product_description": "This is a description of the example product.",
        "price": "19.99",
        "stock_quantity": 100,
        "is_active": true
        }

- **Description:** Updates information for a specific Product.

- **Response Body:**

  .. code-block:: json

    {
    "status": "success",
    "data": {
        "id": 1,
        "product_name": "Example product",
        "product_description": "This is a description of the example product.",
        "price": "19.99",
        "stock_quantity": 100,
        "org_id": 1,
        "created_at": "2024-11-12T06:34:16.731791Z",
        "updated_at": "2024-11-15T06:17:43.591957Z",
        "is_active": true,
        "category": 2,
        "subcategory": null
        }
    }
    
