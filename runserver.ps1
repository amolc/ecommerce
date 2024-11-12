.\env\Scripts\activate
.\scripts\configs\stayvillas.ps1
pip install -r requirements.txt
cd restserver
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:9999