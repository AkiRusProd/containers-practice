# FROM pytorch/pytorch:2.2.1-cuda12.1-cudnn8-runtime
FROM python:3.10-slim

RUN apt update && \
    apt install --no-install-recommends -y build-essential software-properties-common
# RUN apt-get update && apt-get install -y libc6

WORKDIR /app

COPY pyproject.toml /app/pyproject.toml

RUN python -m pip install --upgrade pip && \
    pip install poetry && \
    poetry install

EXPOSE 9000

# COPY backend /app/backend
COPY . /app/backend

# CMD ["poetry", "run", "uvicorn", "backend.src.main:app", "--host", "0.0.0.0", "--port", "9000"]


# docker build -t rag/back -f backend/Dockerfile .
# docker save rag/back -o rag_back.tar
# minikube ssh
# docker load < /path/to/rag_back.tar

# docker build -t rag ./backend/
# docker save rag -o rag.tar
# minikube image load rag.tar

# minikube start --memory=8192 --cpus=2

# minikube delete
# minikube start --memory=16000 --cpus=4
