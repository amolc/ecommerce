import os
import base64
from django.conf import settings
from products.models import Product  # Replace `myapp` with your app's name

# Ensure the static directory exists
STATIC_DIR = os.path.join(settings.BASE_DIR, "static", "product_images")
os.makedirs(STATIC_DIR, exist_ok=True)

import base64
import os
import re

def is_valid_base64(data):
    base64_regex = re.compile(r'^[A-Za-z0-9+/=]+$')
    return bool(base64_regex.match(data))

def save_product_images_and_update_path(product_id=None):
    # If product_id is provided, filter by that ID, else fetch all active products
    if product_id:
        products = Product.objects.filter(id=product_id, is_active=True)
    else:
        products = Product.objects.filter(is_active=True)

    for product in products:
        # Process product_image1
        if product.product_image1:
            # try:
            image_data = product.product_image1
            if image_data.startswith("data:image/png;base64,"):
                image_data = image_data.replace("data:image/png;base64,", "")
            elif image_data.startswith("data:image/jpg;base64,"):
                image_data = image_data.replace("data:image/jpg;base64,", "")

            first_100_chars = image_data[:100]
            # print(f"First 100 characters of image_data: {first_100_chars}")
            if not is_valid_base64(image_data):
                print(f"Invalid base64 data detected for product {image_data}")
            else:
                print("Starting decoding function")
                image_data = base64.b64decode(image_data)
                # print(f"Decoded image_data: {image_data}")
                file_name1 = f"{product.id}_image1.png"
                file_path1 = os.path.join(STATIC_DIR, file_name1)
                with open(file_path1, "wb") as file:
                    file.write(image_data)
                # Update the product_image1 column with the relative path
                product.product_image1 = os.path.join("static", "product_images", file_name1)
                print(f"Saved and updated image1 for product {product.product_image1}")
                # except Exception as e:
                #     print(f"Failed to save image1 for product {product.product_name}: {e}")

        # Process product_image2
        
        if product.product_image2:
            try:
                image_data = product.product_image2
                if image_data.startswith("data:image/png;base64,"):
                    image_data = image_data.replace("data:image/png;base64,", "")
                elif image_data.startswith("data:image/jpg;base64,"):
                    image_data = image_data.replace("data:image/jpg;base64,", "")

                # first_100_chars = image_data[:100]
                print(f"First 100 characters of image_data: {first_100_chars}")
                if not is_valid_base64(image_data):
                    print(f"Invalid base64 data detected for product {image_data}")
                else:
                    print("Starting decoding function")
                    image_data = base64.b64decode(image_data)
                    # print(f"Decoded image_data: {image_data}")
                    file_name2 = f"{product.id}_image2.png"
                    file_path2 = os.path.join(STATIC_DIR, file_name2)
                    with open(file_path2, "wb") as file:
                        file.write(image_data)
                    # Update the product_image1 column with the relative path
                    product.product_image2 = os.path.join("static", "product_images", file_name2)
                    print(f"Saved and updated image2 for product {product.product_image2}")
                # except Exception as e:
                #     print(f"Failed to save image1 for product {product.product_name}: {e}")
            except Exception as e:
                print(f"Failed to save image2 for product {product.product_name}: {e}")

        product.save()

def run():
    save_product_images_and_update_path()