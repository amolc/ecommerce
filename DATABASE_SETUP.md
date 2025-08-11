# Database Setup Guide

## Configuration Options

This project uses MySQL database exclusively across all environments.

### 1. MySQL (Development)

For development environment, use the development settings:

```bash
export DJANGO_SETTINGS_MODULE="restserver.settings.development"
```

This configuration is used by default in the `runserver.sh` script.

### 2. MySQL (Production)

For production environment, use the production settings:

```bash
export DJANGO_SETTINGS_MODULE="restserver.settings.production"
```

This requires:
- MySQL client library installed (`pip install mysqlclient`)
- Connection to the remote MySQL server at `db.pamosapicks.com`
- Database named `pamosapicks`
- Access with user `pamosapicks` and password `10gXWOqeaf!`

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

### 3. MySQL (Local)

For local development with a local MySQL server:

```bash
export DJANGO_SETTINGS_MODULE="restserver.settings.local"
```

This uses the same MySQL configuration as production but can be modified for local development.

## Troubleshooting

If you encounter database connection issues:

### MySQL Issues
1. If you see an error about authentication plugin 'mysql_native_password' not being loaded, this is because MySQL 8+ uses `caching_sha2_password` by default
2. The Django settings have been configured to use this authentication plugin via the 'OPTIONS' setting in the database configuration
3. Verify MySQL connection: `mysql -h db.pamosapicks.com -u pamosapicks -p`
4. Check user credentials and permissions: `mysql -h db.pamosapicks.com -u pamosapicks -p -e "SHOW DATABASES;"`

### General
1. Ensure MySQL client library is installed: `pip install mysqlclient`
2. Check network connectivity to the database server
3. Verify the database credentials in your settings file