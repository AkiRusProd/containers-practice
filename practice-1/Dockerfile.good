# Использование легкого образа
FROM python:3.10-slim

WORKDIR /app

VOLUME /app/data

# Использование .dockerignore, копирование самого необходимого
COPY pyproject.toml /app/pyproject.toml
COPY src /app/src

# Объединение команд для выполнения в одном слое
RUN python -m pip install --upgrade pip && \
    pip install poetry && \
    poetry install

EXPOSE 9000

CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "9000"]