FROM python:3.10-slim

ARG GRADIO_SERVER_PORT=7860
ENV GRADIO_SERVER_PORT=${GRADIO_SERVER_PORT}

WORKDIR /app

# RUN pip install --no-cache-dir gradio
COPY pyproject.toml /app/pyproject.toml

RUN python -m pip install --upgrade pip && \
    pip install poetry && \
    poetry install

EXPOSE 7860

# COPY frontend/webui.py /app/webui.py
COPY webui.py /app/webui.py

CMD ["poetry", "run", "python", "webui.py"]

# docker build -t webui ./frontend
# minikube image load webui
# docker save webui -o webui.tar