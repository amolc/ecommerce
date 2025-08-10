# Category API Documentation

This document describes the Category API endpoints and their usage.

## Overview

The Category API provides comprehensive CRUD (Create, Read, Update, Delete) operations for managing product categories. The API is built using Django REST Framework's ViewSet pattern, which provides a clean and consistent interface.

## Base URL

All category endpoints are prefixed with: `/api/category/`

## Authentication

All endpoints require authentication. Include your authentication token in the request headers:

```
Authorization: Token your_auth_token_here
```

## Endpoints

### 1. List Categories

**GET** `/api/category/categories/`

Retrieves a list of all categories with optional filtering.

**Query Parameters:**
- `is_active` (optional): Filter by active status (`true` or `false`)
- `organisation` (optional): Filter by organisation ID

**Example Request:**
```bash
curl -X GET "http://localhost:8000/api/category/categories/?is_active=true" \
  -H "Authorization: Token your_token"
```

**Example Response:**
```json
{
  "status": "success",
  "message": "Categories retrieved successfully",
  "data": [
    {
      "id": 1,
      "category_name": "Electronics",
      "category_description": "Electronic devices and accessories",
      "is_active": true,
      "category_image": "electronics.jpg",
      "created_at": "2024-01-01T00:00:00Z",
      "updated_at": "2024-01-01T00:00:00Z",
      "organisation": 1
    }
  ],
  "count": 1
}
```

### 2. Create Category

**POST** `/api/category/categories/`

Creates a new category.

**Request Body:**
```json
{
  "category_name": "Electronics",
  "category_description": "Electronic devices and accessories",
  "is_active": true,
  "category_image": "electronics.jpg",
  "organisation": 1
}
```

**Example Request:**
```bash
curl -X POST "http://localhost:8000/api/category/categories/" \
  -H "Content-Type: application/json" \
  -H "Authorization: Token your_token" \
  -d '{
    "category_name": "Electronics",
    "category_description": "Electronic devices and accessories",
    "is_active": true,
    "organisation": 1
  }'
```

**Example Response:**
```json
{
  "status": "success",
  "message": "Category created successfully",
  "data": {
    "id": 1,
    "category_name": "Electronics",
    "category_description": "Electronic devices and accessories",
    "is_active": true,
    "category_image": null,
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z",
    "organisation": 1
  }
}
```

### 3. Retrieve Category

**GET** `/api/category/categories/{id}/`

Retrieves a specific category by ID.

**Example Request:**
```bash
curl -X GET "http://localhost:8000/api/category/categories/1/" \
  -H "Authorization: Token your_token"
```

**Example Response:**
```json
{
  "status": "success",
  "message": "Category retrieved successfully",
  "data": {
    "id": 1,
    "category_name": "Electronics",
    "category_description": "Electronic devices and accessories",
    "is_active": true,
    "category_image": "electronics.jpg",
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z",
    "organisation": 1
  }
}
```

### 4. Update Category (Full Update)

**PUT** `/api/category/categories/{id}/`

Updates a category with all fields (full update).

**Request Body:**
```json
{
  "category_name": "Electronics Updated",
  "category_description": "Updated description",
  "is_active": false,
  "category_image": "new_image.jpg",
  "organisation": 1
}
```

**Example Request:**
```bash
curl -X PUT "http://localhost:8000/api/category/categories/1/" \
  -H "Content-Type: application/json" \
  -H "Authorization: Token your_token" \
  -d '{
    "category_name": "Electronics Updated",
    "category_description": "Updated description",
    "is_active": false,
    "organisation": 1
  }'
```

### 5. Update Category (Partial Update)

**PATCH** `/api/category/categories/{id}/`

Updates only the specified fields of a category.

**Request Body:**
```json
{
  "category_name": "Electronics Updated"
}
```

**Example Request:**
```bash
curl -X PATCH "http://localhost:8000/api/category/categories/1/" \
  -H "Content-Type: application/json" \
  -H "Authorization: Token your_token" \
  -d '{
    "category_name": "Electronics Updated"
  }'
```

### 6. Delete Category

**DELETE** `/api/category/categories/{id}/`

Deletes a specific category.

**Example Request:**
```bash
curl -X DELETE "http://localhost:8000/api/category/categories/1/" \
  -H "Authorization: Token your_token"
```

**Example Response:**
```json
{
  "status": "success",
  "message": "Category \"Electronics\" deleted successfully"
}
```

### 7. List Active Categories

**GET** `/api/category/categories/active/`

Retrieves only active categories.

**Example Request:**
```bash
curl -X GET "http://localhost:8000/api/category/categories/active/" \
  -H "Authorization: Token your_token"
```

### 8. Toggle Category Status

**POST** `/api/category/categories/{id}/toggle_status/`

Toggles the active status of a category.

**Example Request:**
```bash
curl -X POST "http://localhost:8000/api/category/categories/1/toggle_status/" \
  -H "Authorization: Token your_token"
```

**Example Response:**
```json
{
  "status": "success",
  "message": "Category \"Electronics\" deactivated successfully",
  "data": {
    "id": 1,
    "category_name": "Electronics",
    "is_active": false,
    ...
  }
}
```

## Error Responses

All endpoints return consistent error responses:

**400 Bad Request:**
```json
{
  "status": "error",
  "message": "Invalid data provided",
  "errors": {
    "category_name": ["This field is required."]
  }
}
```

**404 Not Found:**
```json
{
  "status": "error",
  "message": "Category not found"
}
```

**500 Internal Server Error:**
```json
{
  "status": "error",
  "message": "Error retrieving categories: Database connection failed"
}
```

## Model Fields

| Field | Type | Description | Required |
|-------|------|-------------|----------|
| id | AutoField | Primary key | Auto-generated |
| category_name | CharField | Name of the category | Yes |
| category_description | TextField | Description of the category | No |
| is_active | BooleanField | Whether the category is active | No (default: True) |
| category_image | TextField | Image URL or path | No |
| created_at | DateTimeField | Creation timestamp | Auto-generated |
| updated_at | DateTimeField | Last update timestamp | Auto-generated |
| organisation | ForeignKey | Associated organisation | Yes |

## Usage Examples

### JavaScript/Fetch API

```javascript
// List categories
const response = await fetch('/api/category/categories/', {
  headers: {
    'Authorization': 'Token your_token'
  }
});
const data = await response.json();

// Create category
const createResponse = await fetch('/api/category/categories/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Token your_token'
  },
  body: JSON.stringify({
    category_name: 'New Category',
    category_description: 'Description',
    organisation: 1
  })
});
```

### Python/Requests

```python
import requests

# List categories
response = requests.get(
    'http://localhost:8000/api/category/categories/',
    headers={'Authorization': 'Token your_token'}
)
categories = response.json()

# Create category
data = {
    'category_name': 'New Category',
    'category_description': 'Description',
    'organisation': 1
}
response = requests.post(
    'http://localhost:8000/api/category/categories/',
    json=data,
    headers={'Authorization': 'Token your_token'}
)
```

## Notes

- All timestamps are in ISO 8601 format
- The API uses database transactions to ensure data consistency
- Category names must be unique within an organisation
- Soft deletion is not implemented; categories are permanently deleted
- The API includes comprehensive error handling and validation
