<<<<<<< HEAD
# /bin/bash
=======
#!/bin/bash
# ps -ef | grep "manage.py runserver" | awk '{print $2}' | xargs kill -9 
>>>>>>> 5ba058317c8dd5601655eb264346067760b275b0
source scripts/configs/stayvillas.sh
source venv/bin/activate
pip install -r requirements.txt
cp -R docs/build/html restserver/static/
cd restserver
python manage.py migrate
<<<<<<< HEAD
python manage.py runserver 0.0.0.0:9999


=======
python manage.py runserver 0.0.0.0:9999
>>>>>>> 5ba058317c8dd5601655eb264346067760b275b0
