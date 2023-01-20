#!/usr/bin/env bash

set -euo pipefail

: "${OPTIONS:=}"

: "${DB_HOST:=localhost}"
: "${DB_PORT:=5432}"
: "${DB_DATABASE:=gamedb}"
: "${DB_USERNAME:=user}"
: "${DB_PASSWORD:=password}"

DATABASE_URL="postgres://${DB_USERNAME}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_DATABASE}?sslmode=disable"

# Check if command exists
if [[ $# -lt 1 ]]; then
    echo -e "A command is required!"
    exit
fi

# Waiting for DB readiness
dbmate --url="${DATABASE_URL}" --wait-timeout=30s wait || exit

# Execute command
if [ "$1" = 'migrate' ]; then
    echo -e "\nStarting DB migrations"
    dbmate --url="${DATABASE_URL}" --migrations-dir=/db/migrations --no-dump-schema up
    echo "DB migrations completed"
elif [ "$1" = 'start' ]; then
    echo -e "\nStarting service ..."
    sleep 3
    exec python3 main.py ${OPTIONS}
else
    exec "$@"
fi