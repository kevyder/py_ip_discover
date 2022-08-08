#!/bin/sh

while ! nc -z database 5432; do sleep 1; done;

alembic upgrade head

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Start the backend...
