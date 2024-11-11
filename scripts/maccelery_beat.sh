#!/usr/bin/env bash

mydir=$(dirname $0)
ps -ef | grep "celery -A restserver worker" | grep -v runcelery | awk '{print $2}' | xargs kill -9

repodir=$(dirname $mydir)
echo $repodir
conffile=/Users/amolc/2020/quantengine/scripts/configs/quantengine.sh
source /Users/amolc/2020/quantengine/scripts/configs/quantengine.sh
cd /Users/amolc/2020/quantengine/restserver
source /Users/amolc/2020/quantengine/venv/bin/activate
celery -A restserver beat --loglevel=debug
#checking if only warning can work