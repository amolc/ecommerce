Booking API
===========

Booking Api for the property booking

GetBooking 
----------

- **Endpoint:** ``GET baseUrl/org_id/api/booking/get-bookings//``

- **Response Body:**

.. code-block:: json

    {
    "status": "success",
    "data": [
        {
            "id": 3,
            "org_id": 1,
            "property_type": "Villa",
            "guest_name": "Onkii",
            "email": "onkii@gmail.com",
            "mobile_no": "9087654321",
            "check_in_date": "2024-09-21",
            "check_out_date": "2024-09-25",
            "num_guests": 2,
            "num_rooms": 1,
            "special_requests": "Late check-in if possible.",
            "total_price": "2500.00"
        }
            ]
    }
GetBookingById
--------------

- **Endpoint:** ``GET /{org_id}/api/booking/get-booking/{Id}/``

- **Response Body:**

.. code-block:: json

    {
    "status": "success",
    "data": {
        "id": 5,
        "org_id": 1,
        "property_type": "Villa",
        "guest_name": "krishna",
        "email": "abc@gmail.com",
        "mobile_no": "7719912920",
        "check_in_date": "2024-09-24",
        "check_out_date": "2024-09-26",
        "num_guests": 2,
        "num_rooms": 2,
        "special_requests": "veg",
        "total_price": "30870.00"
             }
    }


CreateBooking
-------------

- **Endpoint:** ``POST baseUrl/org_id/api/booking/create-booking/``

- **Request Body:**

.. code-block:: json

    {
  "property_type": "Bungalow",
  "guest_name": "vaishaliDeokar",
  "email": "vaishliDeo@example.com",
  "mobile_no": "3214567890",
  "check_in_date": "2023-09-20",
  "check_out_date": "2023-09-25",
  "booking_status": "Pending",
  "num_guests": 4,
  "num_rooms":5,
  "special_requests": "Vegetarian meals",
  "total_price": 500.00
    }


.. - **Response Body:**

.. .. code-block:: json

..     {
    
            
..     }

UpdateBooking
-------------

- **Endpoint:** ``Patch baseUrl/org_id/api/booking/update-booking/{Id}/``
- **Request Body:**

.. code-block:: json

    {
  "property_type": "Bungalow",
  "guest_name": "vaishali kadbhane",
  "email": "johndoe@example.com",
  "mobile_no": "1234567890",
  "check_in_date": "2023-09-20",
  "check_out_date": "2023-09-25",
  "booking_status": "Pending",
  "num_guests": 4,
  "special_requests": "Vegetarian meals",
  "total_price": 500.00
    }


- **Response Body:**

.. code-block:: json

    {
    "status": "success",
    "data": {
        "id": 3,
        "org_id": 1,
        "property_type": "Bungalow",
        "guest_name": "vaishali kadbhane",
        "email": "johndoe@example.com",
        "mobile_no": "1234567890",
        "check_in_date": "2023-09-20",
        "check_out_date": "2023-09-25",
        "num_guests": 4,
        "num_rooms": 1,
        "special_requests": "Vegetarian meals",
        "total_price": "500.00"
            }
    }
