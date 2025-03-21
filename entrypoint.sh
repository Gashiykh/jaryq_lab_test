#!/bin/bash
set -e

until nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
  echo "Ждем подключения к PostgreSQL..."
  sleep 1
done

echo "=== Запуск миграций ==="
python manage.py migrate --noinput

echo "=== Сбор статических файлов ==="
python manage.py collectstatic --noinput

echo "=== Загрузка дефолтных данных ==="
python manage.py loaddata fixtures/restaurant.json fixtures/table.json fixtures/reservation.json

echo "=== Запуск сервера ==="
gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers 3
