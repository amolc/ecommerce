import os
import base64
from django.conf import settings
from products.models import Product  # Replace `myapp` with your app's name

# Ensure the static directory exists
STATIC_DIR = os.path.join(settings.BASE_DIR, "static", "product_images")
os.makedirs(STATIC_DIR, exist_ok=True)

def save_product_images_and_update_path():
    products = Product.objects.filter(is_active=True)  # Fetch active products

    for product in products:
        # Process product_image1
        if product.product_image1:
            try:
                image_data = base64.b64decode(product.product_image1)
                print(image_data)
                file_name1 = f"{product.id}_image1.png"
                file_path1 = os.path.join(STATIC_DIR, file_name1)
                with open(file_path1, "wb") as file:
                    file.write(image_data)
                # Update the product_image1 column with the relative path
                product.product_image1 = os.path.join("static", "product_images", file_name1)
                print(f"Saved and updated image1 for product {product.product_name}")
            except Exception as e:
                print(f"Failed to save image1 for product {product.product_name}: {e}")

        # Process product_image2
        if product.product_image2:
            try:
                image_data = base64.b64decode(product.product_image2)
                file_name2 = f"{product.id}_image2.png"
                file_path2 = os.path.join(STATIC_DIR, file_name2)
                with open(file_path2, "wb") as file:
                    file.write(image_data)
                # Update the product_image2 column with the relative path
                product.product_image2 = os.path.join("static", "product_images", file_name2)
                print(f"Saved and updated image2 for product {product.product_name}")
            except Exception as e:
                print(f"Failed to save image2 for product {product.product_name}: {e}")

        # Save changes to the database
        # product.save()

# Call the function
def run():
    save_product_images_and_update_path()

