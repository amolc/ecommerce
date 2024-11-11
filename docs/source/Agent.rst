Agent API
=========

This document describes the endpoints available for managing property agents.

GetAllAgent
-----------

- **Endpoint:** ``GET http://localhost:8888/1/api/agent/get-agent/``

- **Description:** Retrieves a list of all agents.

- **Response Body:**

  .. code-block:: json

    {
        "status": "success",
        "data": [
            {
                "id": 4,
                "last_login": null,
                "org_id": 1,
                "email": "vaishalikadbhane@gmail.com",
                "password": "pbkdf2_sha256$870000$05CxW5X7crPLLtG1uXvUX8$ah7V65EOpb+Gz6bJdMWMeeSZMvrjwpjK//dc1zuMaRk=",
                "first_name": "vaishali",
                "last_name": "kadbhane",
                "mobile_number": "07719912920",
                "city": "Pune",
                "total_sales": "1000000.00",
                "hire_date": null,
                "is_active": true,
                "is_super_admin": false,
                "is_admin": false,
                "is_agent": true
            }
        ]
    }

GetAgentbyId
------------

- **Endpoint:** ``http://0.0.0.0:8888/api/customer/get-customer/?id=2/``

- **Description:** Fetches details of a specific agent using their ID.

- **Response Body:**

  .. code-block:: json

    {
        "status": "success",
        "data": [
            {
                "id": 9,
                "last_login": null,
                "org_id": 1,
                "email": "agent@gmail.com",
                "password": "pbkdf2_sha256$870000$B8zWENQ1GOW8XEEGgbdc2i$IIZ4pr5jjdDD3DxYTuGotrgiSUJ5Hf7MJ/LcJNdBFxI=",
                "first_name": "John",
                "last_name": "Doe",
                "mobile_number": "1234567890",
                "city": "New York",
                "total_sales": "25000.00",
                "hire_date": null,
                "is_active": true,
                "is_super_admin": false,
                "is_admin": false,
                "is_agent": true
            }
        ]
    }

CreateAgent
-----------

- **Endpoint:** ``http://0.0.0.0:8888/agent/create-agent/``

- **Request Body:**

  .. code-block:: json

    {
        "email": "qwer@gmail.com",
        "password": "qaz",
        "first_name": "John",
        "last_name": "Doe",
        "city": "New York",
        "mobile_number": "1234567890",
        "total_sales": 25000
    }

- **Description:** Adds a new agent to the system.

- **Response Body:**

  .. code-block:: json

    {
        "id": 13,
        "last_login": null,
        "org_id": 1,
        "email": "qwer@gmail.com",
        "first_name": "John",
        "last_name": "Doe",
        "mobile_number": "1234567890",
        "city": "New York",
        "total_sales": "25000.00",
        "hire_date": null,
        "is_active": true,
        "is_super_admin": false,
        "is_admin": false,
        "is_agent": true
    }

LoginAgent
----------

- **Endpoint:** ``http://0.0.0.0:8888/agent/login-agent/``

- **Request Body:**

  .. code-block:: json

    {
        "email": "agent@gmail.com",
        "password": "agent"
    }

- **Description:** Authenticates an agent.

UpdateAgent
-----------

- **Endpoint:** ``http://0.0.0.0:8888/agent/update-agent/{Id}/``

- **Request Body:**

  .. code-block:: json

    {
        "email": "admin@gmail.com",
        "password": "admin@123",
        "first_name": "admin",
        "last_name": "D",
        "mobile_number": "7719912929",
        "city": "Parali",
        "total_sales": "10000.00",
        "hire_date": null,
        "is_active": true,
        "is_super_admin": false,
        "is_admin": false,
        "is_agent": true
    }

- **Description:** Updates information for a specific agent.

- **Response Body:**

  .. code-block:: json

    {
        "status": "success",
        "data": {
            "id": 8,
            "last_login": null,
            "org_id": 1,
            "email": "admin@gmail.com",
            "password": "pbkdf2_sha256$870000$nPNvntukcyTDuJPrqSYWoX$GwIpAXYIvJ8zF/2wUhdP0sYC8Sm2vCGDQWucSD0NJvQ=",
            "first_name": "admin",
            "last_name": "D",
            "mobile_number": "7719912929",
            "city": "Mumbai",
            "total_sales": "10000.00",
            "hire_date": null,
            "is_active": true,
            "is_super_admin": false,
            "is_admin": false,
            "is_agent": true
        }
    }
