#!/bin/bash

NAME="restserver-daphne"  # Name of the application
DJANGOVDIR=/home/ubuntu/quantengine # Django project directory
DJANGODIR=/home/ubuntu/quantengine/restserver # Django project directory
DJANGOENVDIR=/home/ubuntu/repos/quantengine/scripts/configs/ns1engine.sh # Django project env

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /home/ubuntu/quantengine/venv/bin/activate
source $DJANGOENVDIR

# Start daphne
exec daphne  -p 7778 restserver.asgi:application
