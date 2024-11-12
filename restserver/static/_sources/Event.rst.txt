Event API
==========

This document describes the (Create, Read, Update) operations for the `Event` model in the application.

**Event Model**



The `Event` model represents a user in the system and includes the following fields:

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

- `baseurl`` = "http://localhost:7777/1/api/"

**Production URL:**

- `baseurl`` = "https://api.sunandsandapi.com/1/api/"

.. Event


GetEvent 
----------

- **Endpoint:** ``GET baseUrl/org_id/api/event/get-event/``

- **Response Body:**

.. code-block:: json

    {
        "status": "success",
        "data": {
            "id": 2,
            "org_id": 1,
            "first_name": "Krishna",
            "last_name": "Lavhare",
            "email": "janedoe@example.com",
            "mobile_no": "9876543210",
            "concern": "New Booking",
            "property_location": "Sunset Blvd, Los Angeles",
            "message": "I am interested in booking the villa for next week."
        }
    }
GetEnquiryById
--------------

- **Endpoint:** ``GET /{org_id}/api/enquiry/get-enquiry/{Id}/``

- **Response Body:**

.. code-block:: json

    {
        "status": "success",
        "data": {
            "id": 2,
            "org_id": 1,
            "first_name": "Krishna",
            "last_name": "Lavhare",
            "email": "janedoe@example.com",
            "mobile_no": "9876543210",
            "concern": "New Booking",
            "property_location": "Sunset Blvd, Los Angeles",
            "message": "I am interested in booking the villa for next week."
    }


CreateEvent
-------------

- **Endpoint:** ``POST baseUrl/org_id/api/event/create-event/``

- **Request Body:**

.. code-block:: json

    {
    "first_name": "admin",
    "last_name": "Deokar",
    "email": "deokar@example.com",
    "mobile_no": "98767210",
    "concern": "New Booking",
    "property_location": "Sunset Blvd, Los Angeles",
    "message": "I am interested in booking the villa for next week."
    }


- **Response Body:**

.. code-block:: json

    {
    "status": "success",
    "data": {
        "id": 6,
        "org_id": 1,
        "first_name": "admin",
        "last_name": "Deokar",
        "email": "deokar@example.com",
        "mobile_no": "98767210",
        "concern": "New Booking",
        "property_location": "Sunset Blvd, Los Angeles",
        "message": "I am interested in booking the villa for next week."
            }
    }

UpdateEvent
-------------

- **Endpoint:** ``Patch baseUrl/org_id/api/event/update-event/{Id}/``
- **Request Body:**

.. code-block:: json

    {
    "first_name": "Krishna",
    "last_name": "Lavhare",
    "email": "janedoe@example.com",
    "mobile_no": "9876543210",
    "concern": "New Booking",
    "property_location": "Sunset Blvd, Los Angeles",
    "message": "I am interested in booking the villa for next week."
    }

- **Response Body:**

.. code-block:: json

    {
    "status": "success",
    "data": {
        "id": 6,
        "org_id": 1,
        "first_name": "Krishna",
        "last_name": "Lavhare",
        "email": "janedoe@example.com",
        "mobile_no": "9876543210",
        "concern": "New Booking",
        "property_location": "Sunset Blvd, Los Angeles",
        "message": "I am interested in booking the villa for next week."
            }
    }