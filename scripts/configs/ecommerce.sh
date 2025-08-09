#!/usr/bin/env bash
# exporting env variables to be used with django server
export DJANGO_SETTINGS_MODULE="restserver.settings.development"
export SERVICE_PORT=9999
export MYSQL_USER="pamosapicks"
export MYSQL_DB="pamosapicks"
export MYSQL_HOST="db.pamosapicks.com"
export MYSQL_PASSWORD="10gXWOqeaf!"
export MYSQL_PORT="5432"
export CELERY_URL="amqp://localhost"
export REDIS_HOST="127.0.0.1"
export REDIS_PORT="6379"

# config for api server
REPO_DIR="/home/ubuntu/repos/ecommerce"
REPO_BRANCH="main"
PROJECT_DEST="/home/ubuntu/ecommerce"
APISERVER="restserver"
STATIC_DIR="/home/ubuntu/ecommerce/static"
EXCLUDE_DIRS="logs/ /.git/ /datafeed/csv/ venv/"


