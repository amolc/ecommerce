# Database Setup Guide

## Configuration Options

This project supports multiple database configurations:

### 1. SQLite (Local Development)

The simplest option for local development is to use SQLite, which requires no additional setup:

```bash
export DJANGO_SETTINGS_MODULE="restserver.settings.local"
```

This configuration is used by default in the `runserver.sh` script.

### 2. MySQL (Development)

For a more production-like environment, you can use MySQL:

```bash
export DJANGO_SETTINGS_MODULE="restserver.settings.development"
```

This requires:
- MySQL client library installed (`pip install mysqlclient`)
- Local MySQL server running (or connection to a remote MySQL server)
- Database named `flipopo_dev`
- Access with user `pamosapicks` and password `10gXWOqeaf1`

To set up a local MySQL server on macOS:

```bash
# Install MySQL server and client
brew install mysql

# Start MySQL service
brew services start mysql

# Create database and user
echo "CREATE DATABASE IF NOT EXISTS flipopo_dev; \
      CREATE USER IF NOT EXISTS 'pamosapicks'@'localhost' IDENTIFIED BY '10gXWOqeaf1'; \
      GRANT ALL PRIVILEGES ON flipopo_dev.* TO 'pamosapicks'@'localhost'; \
      FLUSH PRIVILEGES;" | mysql -u root

# Install the Python connector
pip install mysqlclient

# Note: MySQL 8+ uses caching_sha2_password authentication by default
# The Django settings have been configured to use this authentication plugin
```

Alternatively, you can connect to the remote MySQL database at `db.pamosapicks.com` by changing the HOST setting in development.py.

### 3. PostgreSQL (Production)

The production configuration uses environment variables for connection details:

```bash
export DJANGO_SETTINGS_MODULE="restserver.settings.production"
```

Environment variables are typically set in `scripts/configs/ecommerce.sh`.

## Troubleshooting

If you encounter database connection issues:

### PostgreSQL Issues
1. Verify PostgreSQL is running: `pg_isready -h localhost -p 5432`
2. Check user credentials if using PostgreSQL
3. Ensure psycopg2 is properly installed: `pip install --force-reinstall psycopg2-binary`

### MySQL Issues
1. If you see an error about authentication plugin 'mysql_native_password' not being loaded, this is because MySQL 8+ uses `caching_sha2_password` by default
2. The Django settings have been configured to use this authentication plugin via the 'OPTIONS' setting in development.py
3. Verify MySQL is running: `brew services list | grep mysql`
4. Check user credentials and permissions: `mysql -u root -e "SELECT User, Host, plugin FROM mysql.user WHERE User = 'pamosapicks';"` 

### General
1. For simplicity, switch to SQLite for local development