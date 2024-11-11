#!/bin/bash

NAME="restserver-daphne"  # Name of the application
DJANGOVDIR=/var/www/quantengine # Django project directory
DJANGODIR=/var/www/quantengine/restserver # Django project directory
DJANGOENVDIR=/home/ubuntu/repos/quantengine/scripts/configs/quantengine.sh # Django project env

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /var/www/quantengine/venv/bin/activate
source $DJANGOENVDIR

# Start daphne
exec daphne  -p 7778 restserver.asgi:application
