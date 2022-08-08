FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

ENV PYTHONPATH "${PYTHONPATH}:/"
ENV PORT=8000

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy using poetry.lock* in case it doesn't exist yet
COPY ./pyproject.toml ./poetry.lock* /app/

COPY ./alembic.ini /app/

COPY ./startup.sh /app/

COPY ./migrations /app/migrations/

COPY ./tests /app/tests/

RUN poetry install --no-root

RUN chmod 755 ./startup.sh

RUN apt-get update && apt-get install -y netcat

COPY ./app /app

CMD ["./startup.sh"]
