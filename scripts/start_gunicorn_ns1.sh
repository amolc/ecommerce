#!/usr/bin/env bash

# if [ -z $SUPERVISED_DJANGO_SITE ]
# then
#     echo "This script only works for supervisor mode"
#     exit 0
# fi

mydir=$(dirname $0)

repodir=$(dirname $mydir)
conffile=/home/ubuntu/repos/quantengine/scripts/configs/ns1engine.sh
source $conffile
DJANGO_BASE_DIR=$PROJECT_DEST/$APISERVER
site=$SUPERVISED_DJANGO_SITE
####################### Add supervisor non daemon mode




# gunicorn_conf_file=$DJANGO_BASE_DIR/$site/gunicorn_conf.py
# # Remove redundant slashes
# gunicorn_conf_file=$(echo $gunicorn_conf_file | sed s#//*#/#g)

# is_supervised=$(grep SUPERVISED_DJANGO_SITE $gunicorn_conf_file)
# if [ -z "$is_supervised" ]
# then
# echo """

# if 'SUPERVISED_DJANGO_SITE' in os.environ: daemon = False

# """ >> $gunicorn_conf_file
# fi
# ####################### END: Add supervisor non daemon mode





# # SERVICE_PORT_OVERRIDE can me mentioned in supervisor conf
# if [[ ! -z $SERVICE_PORT_OVERRIDE ]]
# then
#     export SERVICE_PORT=$SERVICE_PORT_OVERRIDE
# fi

# if [[ ! -z $SERVICE_PORT ]]
# then
#     fuser -k -n tcp $SERVICE_PORT
# fi
echo "$USER"

cd $DJANGO_BASE_DIR
source /home/ubuntu/quantengine/venv/bin/activate
/home/ubuntu/quantengine/venv/bin/gunicorn --bind 0.0.0.0:7777 restserver.wsgi:application
# gunicorn -c $site/gunicorn_conf.py $site.wsgi:application

