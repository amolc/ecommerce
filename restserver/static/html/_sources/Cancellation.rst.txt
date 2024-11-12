Cancellation API
========================

This document describes the (Create, Read, Update) operations for the `Cancellation model` in the application.

**Cancellation Model**



The `Cancellation` model represents a user in the system and includes the following fields:

- `org_id` (integer): The organization ID associated with the customer.
- `email` (string): The email address of the customer.
- `first_name` (string): The first name of the customer.
- `last_name` (string): The last name of the customer.
- `mobile_number` (string): The mobile phone number of the customer.
- `Concern` (string): The subject or primary concern of the enquiry
- `Property_Location` (string): The location of the property related to the enquiry
- `Message` (string): Additional information or message provided by the customer.

**URL**

**Local Development URL:**

- `Baseurl`` = "http://localhost:7777/1/api/"

**Production URL:**

- `baseurl`` = "https://api.sunandsandapi.com/1/api/"

.. Cancellation
.. ============

GetCancellation
---------------

- **Endpoint:** ``GET baseUrl/org_id/api/cancellation/get-cancellation/``

- **Response Body:**

.. code-block:: json

    {
    "status": "success",
    "data": [
        {
            "id": 4,
            "org_id": 1,
            "booking_reference": "ABC1423",
            "name": "Krishna Lavhare",
            "email": "john@example.com",
            "mobile_no": "1234567890",
            "reason": "Personal reasons"
        }
            ]
    }

GetCancellationById
-------------------

- **Endpoint:** ``GET /{org_id}/api/cancellation/get-cancellation/{Id}/``

- **Response Body:**

.. code-block:: json

    {
    "status": "success",
    "data": {
        "id": 4,
        "org_id": 1,
        "booking_reference": "ABC1423",
        "name": "Krishna Lavhare",
        "email": "john@example.com",
        "mobile_no": "1234567890",
        "reason": "Personal reasons"
            }
    }


CreateCancellation
------------------

- **Endpoint:** ``POST baseUrl/org_id/api/enquiry/create-enquiry/``

- **Request Body:**

.. code-block:: json

    {
  "booking_reference": "qwe1423",
  "name": "vaishali",
  "email": "vaishali@example.com",
  "mobile_no": "3456767890",
  "reason": "Holiday"
    }


- **Response Body:**

.. code-block:: json

    {
    "status": "success",
    "data": {
        "id": 5,
        "org_id": 1,
        "booking_reference": "qwe1423",
        "name": "vaishali",
        "email": "vaishali@example.com",
        "mobile_no": "3456767890",
        "reason": "Holiday"
            }
    }

UpdateEnquiry
-------------

- **Endpoint:** ``Patch baseUrl/org_id/api/cancellation/update-cancellation/{Id}/``
- **Request Body:**

.. code-block:: json

    {
  "booking_reference": "34561423",
  "name": "Vaishalik",
  "email": "vbk@example.com",
  "mobile_no": "1234567890",
  "reason": "Personal reasons"
    }


- **Response Body:**

.. code-block:: json

    {
    "status": "success",
    "data": {
        "id": 5,
        "org_id": 1,
        "booking_reference": "34561423",
        "name": "Vaishalik",
        "email": "vbk@example.com",
        "mobile_no": "1234567890",
        "reason": "Personal reasons"
            }
    }