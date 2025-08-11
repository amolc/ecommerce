# Category API Postman Collection Guide

This guide will help you set up and use the Postman collection for testing the Category API endpoints.

## 📁 Files Included

1. **`Category_API.postman_collection.json`** - Main collection with all API endpoints
2. **`Category_API_Environment.postman_environment.json`** - Environment variables
3. **`POSTMAN_GUIDE.md`** - This guide

## 🚀 Quick Setup

### Step 1: Import Collection and Environment

1. **Open Postman**
2. **Import Collection:**
   - Click "Import" button
   - Select `Category_API.postman_collection.json`
   - Click "Import"

3. **Import Environment:**
   - Click "Import" button
   - Select `Category_API_Environment.postman_environment.json`
   - Click "Import"

### Step 2: Configure Environment

1. **Select Environment:**
   - In the top-right corner, select "Category API Environment"

2. **Update Variables (if needed):**
   - Click the environment name → "Edit"
   - Update variables as needed:
     - `base_url`: Your Django server URL (default: `http://localhost:9999`)
     - `org_id`: Your organisation ID (default: `1`)

### Step 3: Start Django Server

```bash
# Navigate to your Django project
cd /path/to/your/ecommerce/restserver

# Activate virtual environment (if using one)
source venv/bin/activate

# Start the development server
python manage.py runserver
```

## 📋 Available Endpoints

### 🔍 **Read Operations**

| Endpoint | Method | Description |
|----------|--------|-------------|
| `{{base_url}}/{{org_id}}/api/category/categories/` | GET | List all categories |
| `{{base_url}}/{{org_id}}/api/category/categories/?is_active=true` | GET | List categories with filter |
| `{{base_url}}/{{org_id}}/api/category/categories/active/` | GET | List only active categories |
| `{{base_url}}/{{org_id}}/api/category/categories/{{category_id}}/` | GET | Get specific category |

### ➕ **Create Operations**

| Endpoint | Method | Description |
|----------|--------|-------------|
| `{{base_url}}/{{org_id}}/api/category/categories/` | POST | Create new category |
| `{{base_url}}/{{org_id}}/api/category/categories/` | POST | Create Books category |
| `{{base_url}}/{{org_id}}/api/category/categories/` | POST | Create Clothing category |

### ✏️ **Update Operations**

| Endpoint | Method | Description |
|----------|--------|-------------|
| `{{base_url}}/{{org_id}}/api/category/categories/{{category_id}}/` | PUT | Full update |
| `{{base_url}}/{{org_id}}/api/category/categories/{{category_id}}/` | PATCH | Partial update |
| `{{base_url}}/{{org_id}}/api/category/categories/{{category_id}}/toggle_status/` | POST | Toggle active status |

### 🗑️ **Delete Operations**

| Endpoint | Method | Description |
|----------|--------|-------------|
| `{{base_url}}/{{org_id}}/api/category/categories/{{category_id}}/` | DELETE | Delete category |

## 🧪 Testing Workflow

### 1. **Initial Setup**
```
1. Start Django server
2. Import collection and environment
3. Select "Category API Environment"
```

### 2. **Create Test Data**
```
1. Run "Create Category" to create your first category
2. Note the category ID from the response
3. The category_id will be automatically stored in environment variables
```

### 3. **Test CRUD Operations**
```
1. List Categories - Verify your category appears
2. Get Category by ID - Retrieve specific category
3. Update Category - Test both PUT and PATCH
4. Toggle Status - Test the custom action
5. Delete Category - Remove the category
```

### 4. **Test Error Scenarios**
```
1. Create Category - Invalid Data (empty name)
2. Create Category - Duplicate Name
3. Get Category - Not Found (ID: 999)
4. Update Category - Not Found
5. Delete Category - Not Found
```

## 📝 Request Body Examples

### Create Category
```json
{
  "category_name": "Electronics",
  "category_description": "Electronic devices and accessories",
  "is_active": true,
  "category_image": "electronics.jpg",
  "organisation": 1
}
```

### Update Category (Full)
```json
{
  "category_name": "Electronics Updated",
  "category_description": "Updated electronic devices and accessories",
  "is_active": true,
  "category_image": "electronics_updated.jpg",
  "organisation": 1
}
```

### Update Category (Partial)
```json
{
  "category_name": "Electronics Partially Updated",
  "is_active": false
}
```

## 🔍 Expected Responses

### Success Response (200/201)
```json
{
  "status": "success",
  "message": "Category created successfully",
  "data": {
    "id": 1,
    "category_name": "Electronics",
    "category_description": "Electronic devices and accessories",
    "is_active": true,
    "category_image": "electronics.jpg",
    "created_at": "2024-01-26T12:00:00Z",
    "updated_at": "2024-01-26T12:00:00Z",
    "organisation": 1
  }
}
```

### Error Response (400)
```json
{
  "status": "error",
  "message": "Invalid data provided",
  "errors": {
    "category_name": ["This field is required."]
  }
}
```

### Not Found Response (404)
```json
{
  "detail": "Not found."
}
```

## 🎯 Testing Tips

### 1. **Use Environment Variables**
- The collection automatically stores `category_id` from create responses
- Use `{{category_id}}` in subsequent requests

### 2. **Test Data Setup**
- Use "Create Test Categories" to quickly populate your database
- Run "List Categories" to verify data creation

### 3. **Error Testing**
- The "Error Tests" folder contains all error scenarios
- Test these after successful operations

### 4. **Filtering**
- Test different filter combinations:
  - `?is_active=true`
  - `?is_active=false`
  - `?organisation=1`

## 🔧 Troubleshooting

### Common Issues

1. **Connection Refused**
   - Ensure Django server is running on `http://localhost:9999`
   - Check if port 9999 is available

2. **404 Not Found**
   - Verify the URL structure is correct
   - Check if the category ID exists

3. **400 Bad Request**
   - Validate JSON format in request body
   - Check required fields (category_name, organisation)

4. **500 Internal Server Error**
   - Check Django server logs
   - Verify database migrations are applied

### Debug Steps

1. **Check Server Status**
   ```bash
   python manage.py runserver
   ```

2. **Verify Database**
   ```bash
   python manage.py migrate
   python manage.py check
   ```

3. **Test with curl**
   ```bash
   curl -X GET "http://localhost:9999/1/api/category/categories/"
   ```

## 📊 Test Scenarios

### Complete Workflow Test
1. Create category
2. List all categories
3. Get category by ID
4. Update category (full)
5. Update category (partial)
6. Toggle status
7. Delete category

### Error Handling Test
1. Create with invalid data
2. Create duplicate category
3. Access non-existent category
4. Update non-existent category
5. Delete non-existent category

### Filtering Test
1. List all categories
2. List active categories only
3. List inactive categories only
4. Use custom active endpoint

## 🎉 Success Criteria

Your API is working correctly if:

✅ All CRUD operations return appropriate status codes  
✅ Response format matches expected structure  
✅ Error scenarios return proper error messages  
✅ Filtering works as expected  
✅ Custom actions (toggle_status, active) function correctly  
✅ Environment variables are automatically updated  

## 📞 Support

If you encounter issues:

1. Check Django server logs
2. Verify environment variables
3. Test with curl or browser
4. Review the test documentation in `TEST_DOCUMENTATION.md`

Happy testing! 🚀
