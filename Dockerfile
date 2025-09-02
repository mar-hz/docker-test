FROM python:latest

ENV PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1

WORKDIR /app
COPY . .
RUN pip install flask Flask-BasicAuth

EXPOSE 3000
CMD ["python", "app.py"]
