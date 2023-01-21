#!/usr/bin/env bash

set -euo pipefail


DATABASE_URL="postgres://user:password@db:5432/gamedb?sslmode=disable"

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
    dbmate --url="${DATABASE_URL}" --migrations-dir=./db/migrations --no-dump-schema up
    echo "DB migrations completed"
elif [ "$1" = 'start' ]; then
    echo -e "\nStarting service ..."
    sleep 3
    exec flask --debug run --host 0.0.0.0 --port 8000
else
    exec "$@"
fi