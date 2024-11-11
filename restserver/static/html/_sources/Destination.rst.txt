Destination API
===============

This document describes the (Create, Read, Update) operations for the `Destination` model in the application.

**Destination Model**


The `Destination` model represents a user in the system and includes the following fields:

- `Id` (integer) A unique identifier for the destination.
- `country` (string) The country where the destination is located.
- `city` (string) The city where the destination is located.
- `img` A field that stores the image or image URL of the destination.

**URL**

**Local Development URL:**

- `baseurl`` = "http://localhost:7777/1/api/"

**Production URL:**

- `baseurl`` = "https://api.sunandsandapi.com/1/api/"

.. Destination
.. ===========

GetDestination 
--------------

- **Endpoint:** ``GET baseUrl/org_id/api/destination/destinations/``

- **Response Body:**

.. code-block:: json

    {
    "status": "success",
    "data": [
        {
            "id": 59,
            "country": "India",
            "city": "Mussorie",
            "img": "https://www.sunandsandstays.com/assets/img/Mussoorie.svg"
        },


CreateDestination
-----------------

- **Endpoint:** ``POST baseUrl/org_id/api/destination/destinations/``

- **Request Body:**

.. code-block:: json

    {
    "country": "India",
    "city": "Nashik",
    "img": "https://www.sunandsandstays.com/assets/img/Jaipur.svg"
    }

- **Response Body:**

.. code-block:: json

    {
    "id": 70,
    "country": "India",
    "city": "Nashik",
    "img": "https://www.sunandsandstays.com/assets/img/Jaipur.svg"
    }

UpdateDestination
-----------------

- **Endpoint:** ``Patch baseUrl/org_id/api/destination/destinations/{Id}/``
- **Request Body:**

.. code-block:: json

    {
    "country": "India",
    "city": "Sinner",
    "img": "https://www.sunandsandstays.com/assets/img/Kasauli.svg"
    }

- **Response Body:**

.. code-block:: json

    {
    "status": "success",
    "data": {
        "id": 70,
        "country": "India",
        "city": "Sinner",
        "img": "https://www.sunandsandstays.com/assets/img/Kasauli.svg"
            }
    }