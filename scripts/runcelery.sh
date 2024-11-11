#!/usr/bin/env bash

mydir=$(dirname $0)
ps -ef | grep "celery -A restserver worker" | grep -v runcelery | awk '{print $2}' | xargs kill -9

repodir=$(dirname $mydir)
echo $repodir
conffile=/home/ubuntu/repos/quantengine/scripts/configs/quantengine.sh
source /home/ubuntu/repos/quantengine/scripts/configs/quantengine.sh
cd /var/www/quantengine/restserver
source /var/www/quantengine/venv/bin/activate
celery -A restserver worker --loglevel=debug
#checking if only warning can work
