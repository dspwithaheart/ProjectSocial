#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi


if [ "$DATABASE" = "mongo" ]
then
    echo "Waiting for mongo..."

    while ! nc -z $MONGO_DB_HOST $MONGO_DB_PORT; do
      sleep 0.1
    done

    echo "mongo started"
fi
python manage.py flush --no-input
# python manage.py makemigrations hello_django
python manage.py migrate

exec "$@"
