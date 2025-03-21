#!/bin/bash
set -e

echo "=== Запуск миграций ==="
python manage.py migrate --noinput

echo "=== Загрузка дефолтных данных ==="
python manage.py loaddata fixtures/restaurant.json fixtures/table.json fixtures/reservation.json

echo "=== Запуск сервера ==="
python manage.py runserver 0.0.0.0:8000
