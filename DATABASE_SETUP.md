# Database Setup Guide

## Configuration Options

This project supports multiple database configurations:

### 1. SQLite (Local Development)

The simplest option for local development is to use SQLite, which requires no additional setup:

```bash
export DJANGO_SETTINGS_MODULE="restserver.settings.local"
```

This configuration is used by default in the `runserver.sh` script.

### 2. PostgreSQL (Development)

For a more production-like environment, you can use PostgreSQL locally:

```bash
export DJANGO_SETTINGS_MODULE="restserver.settings.development"
```

This requires:
- PostgreSQL installed and running on your machine
- A database named `flipopo_dev`
- A user named `flipopo_dev` with password `!Xdasdf890`

To create the required database and user:

```bash
# Connect to PostgreSQL as a superuser
psql -U postgres

# Create the user and database
CREATE USER flipopo_dev WITH PASSWORD '!Xdasdf890';
CREATE DATABASE flipopo_dev OWNER flipopo_dev;
```

### 3. PostgreSQL (Production)

The production configuration uses environment variables for connection details:

```bash
export DJANGO_SETTINGS_MODULE="restserver.settings.production"
```

Environment variables are typically set in `scripts/configs/ecommerce.sh`.

## Troubleshooting

If you encounter database connection issues:

1. Verify PostgreSQL is running: `pg_isready -h localhost -p 5432`
2. Check user credentials if using PostgreSQL
3. Ensure psycopg2 is properly installed: `pip install --force-reinstall psycopg2-binary`
4. For simplicity, switch to SQLite for local development