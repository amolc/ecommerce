#!/bin/bash
ps -ef | grep "manage.py runserver" | awk '{print $2}' | xargs kill -9 

# Use MySQL development settings by default
export DJANGO_SETTINGS_MODULE="restserver.settings.development"

# Set MySQL client environment variables
export LDFLAGS="-L/opt/homebrew/opt/mysql-client/lib"
export CPPFLAGS="-I/opt/homebrew/opt/mysql-client/include"
export PKG_CONFIG_PATH="/opt/homebrew/opt/mysql-client/lib/pkgconfig"

source venv/bin/activate
pip install -r requirements.txt
# cp -R docs/build/html restserver/static/
cd restserver
python manage.py migrate

python manage.py runserver 0.0.0.0:9999


