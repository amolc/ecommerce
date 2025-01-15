.\env\Scripts\activate
.\scripts\configs\ecommerce.ps1

pip install -r requirements.txt
Set-Location restserver

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:9999