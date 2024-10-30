FROM pytorch/pytorch:2.2.1-cuda12.1-cudnn8-runtime

RUN apt update && \
    apt install --no-install-recommends -y build-essential software-properties-common
# RUN apt-get update && apt-get install -y libc6

WORKDIR /app

COPY pyproject.toml /app/pyproject.toml

RUN python -m pip install --upgrade pip && \
    pip install poetry && \
    poetry install

EXPOSE 9000

COPY backend /app/backend

CMD ["poetry", "run", "uvicorn", "backend.src.main:app", "--host", "0.0.0.0", "--port", "9000"]
