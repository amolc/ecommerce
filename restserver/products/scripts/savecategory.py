import os
import base64
from django.conf import settings
from products.models import Product, ProductCategory # Replace `myapp` with your app's name

# Ensure the static directory exists
STATIC_DIR = os.path.join(settings.BASE_DIR, "static", "category_images")
os.makedirs(STATIC_DIR, exist_ok=True)

import base64
import os
import re

def is_valid_base64(data):
    base64_regex = re.compile(r'^[A-Za-z0-9+/=]+$')
    return bool(base64_regex.match(data))


def save_category_images_and_update_path(category_id=None):
    # If product_id is provided, filter by that ID, else fetch all active products
    if category_id:
        categories = ProductCategory.objects.filter(id=category_id)
    else:
        categories = ProductCategory.objects.filter()

    for category in categories:
        # Process product_image1
        if category.category_image:
            # try:
            image_data = category.category_image
            if image_data.startswith("data:image/png;base64,"):
                image_data = image_data.replace("data:image/png;base64,", "")
            elif image_data.startswith("data:image/jpeg;base64,"):
                image_data = image_data.replace("data:image/jpeg;base64,", "")
            elif image_data.startswith("data:image/webp;base64,"):
                image_data = image_data.replace("data:image/webp;base64,", "")
            

            first_100_chars = image_data[:100]
            print(f"First 100 characters of image_data: {first_100_chars}")
           
            if not is_valid_base64(image_data):
                print(f"Invalid base64 data detected for category")
               
            else:
                print("Starting decoding function")
                image_data = base64.b64decode(image_data)
                # print(f"Decoded image_data: {image_data}")
                file_name1 = f"{category.id}_image.png"
                file_path1 = os.path.join(STATIC_DIR, file_name1)
                with open(file_path1, "wb") as file:
                    file.write(image_data)
                # Update the product_image1 column with the relative path
                category.category_image = os.path.join("static", "category_images", file_name1)
                print(f"Saved and updated image1 for product {category.category_name}")
                # except Exception as e:
                #     print(f"Failed to save image1 for product {product.product_name}: {e}")
                category.save()

       

def run():
    save_category_images_and_update_path()