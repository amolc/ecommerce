#!/usr/bin/env bash
mydir=$(dirname $0)

repodir=$(dirname $mydir)
conffile=/home/ubuntu/repos/quantengine/scripts/configs/quantengine.sh
source $conffile

DJANGO_BASE_DIR=$PROJECT_DEST/$APISERVER
DJANGO_VENV_DIR=$PROJECT_DEST
source /var/www/quantengine/venv/bin/activate

cd $DJANGO_BASE_DIR
celery -A restserver beat --loglevel=debug
