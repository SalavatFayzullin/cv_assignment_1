#!/bin/bash
set -e

# Wait for postgres
if [ "$1" = "webserver" ]; then
    echo "Waiting for postgres..."
    while ! nc -z postgres 5432; do
        sleep 1
    done
    echo "PostgreSQL started"
    
    # Initialize database
    echo "Initializing Airflow database..."
    airflow db init
    
    # Create admin user if it doesn't exist
    echo "Creating admin user..."
    airflow users create \
        --username "${_AIRFLOW_WWW_USER_USERNAME:-admin}" \
        --firstname "${_AIRFLOW_WWW_USER_FIRSTNAME:-Admin}" \
        --lastname "${_AIRFLOW_WWW_USER_LASTNAME:-User}" \
        --role "${_AIRFLOW_WWW_USER_ROLE:-Admin}" \
        --email "${_AIRFLOW_WWW_USER_EMAIL:-admin@example.com}" \
        --password "${_AIRFLOW_WWW_USER_PASSWORD:-admin}" || echo "User already exists"
    
    # Start webserver
    exec airflow webserver
    
elif [ "$1" = "scheduler" ]; then
    echo "Waiting for postgres..."
    while ! nc -z postgres 5432; do
        sleep 1
    done
    echo "PostgreSQL started"
    
    # Wait for webserver to initialize DB
    echo "Waiting for database initialization..."
    sleep 30
    
    # Start scheduler
    exec airflow scheduler
else
    # Execute any other command
    exec "$@"
fi