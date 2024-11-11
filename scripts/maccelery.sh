#!/usr/bin/env bash

mydir=$(dirname $0)
ps -ef | grep "celery -A restserver worker" | grep -v runcelery | awk '{print $2}' | xargs kill -9

repodir=$(dirname $mydir)
echo $repodir
conffile=$repodir/scripts/configs/quantengine.sh
source $repodir/scripts/configs/quantengine.sh
cd $repodir/restserver
source $repodir/restserver/venv/bin/activate
celery -A restserver worker --loglevel=debug
#checking if only warning can work
