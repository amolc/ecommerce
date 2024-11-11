#!/bin/bash
ps -ef | grep "python manage.py runserver" | awk '{print $2}' | xargs kill -9 
source scripts/configs/stayvillas.sh
source venv/bin/activate
pip install -r requirements.txt
cp -R docs/build/html restserver/static/
cd restserver
python manage.py migrate
python manage.py runserver 0.0.0.0:8888


