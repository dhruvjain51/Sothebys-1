#!/bin/bash

while ! mysqladmin ping -h"db" --silent; do
	echo sleeping for db;
    sleep 1;
done;

python manage.py migrate

python manage.py runserver 0.0.0.0:8000

