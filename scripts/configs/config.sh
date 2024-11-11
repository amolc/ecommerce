#!/usr/bin/env bash
# exporting env variables to be used with django server
export DJANGO_SETTINGS_MODULE="restserver.settings"
export SERVICE_PORT=7777
export MYSQL_USER="stockrobot"
export MYSQL_DB="quantengine"
export MYSQL_HOST="db.iamstockbot.com"
export MYSQL_PASSWORD="10gXWOqeaf"
export MYSQL_PORT="5432"
export CELERY_URL="amqp://localhost"
export REDIS_HOST="127.0.0.1"
export REDIS_PORT="6379"

# config for api server
REPO_DIR="/home/ubuntu/repos/quantengine"
REPO_BRANCH="main"
PROJECT_DEST="/var/www/quantengine"
APISERVER="restserver"
STATIC_DIR="/var/www/static"
EXCLUDE_DIRS="logs/ /.git/ /datafeed/csv/"

# supervisor names
# to disable any service comment its name
APISUPERVISORNAME="apiserver"
CELERYSUPERVISORNAME="quantengine_celery"
CELERYBEATSUPERVISORNAME="quantengine_beat"