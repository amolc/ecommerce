#!/usr/bin/env bash
# exporting env variables to be used with django server
export DJANGO_SETTINGS_MODULE="restserver.settings"
export SERVICE_PORT=7777
export MYSQL_USER="stockrobot"
export MYSQL_DB="stayvillas"
export MYSQL_HOST="api.stayvillas.co"
export MYSQL_PASSWORD="10gXWOqeaf"
export MYSQL_PORT="5432"
export CELERY_URL="amqp://localhost"
export REDIS_HOST="127.0.0.1"
export REDIS_PORT="6379"

# config for api server
REPO_DIR="/home/ubuntu/repos/stayvillas-api"
REPO_BRANCH="main"
PROJECT_DEST="/home/ubuntu/stayvillas-api"
APISERVER="restserver"
STATIC_DIR="/home/ubuntu/stayvillas-api/static"
EXCLUDE_DIRS="logs/ /.git/ /datafeed/csv/ venv/"

# supervisor names
# to disable any service comment its name
APISUPERVISORNAME="stayvillasapiserver"
CELERYSUPERVISORNAME="stayvillas_celery"
CELERYBEATSUPERVISORNAME="stayvillas_celery_beat"

