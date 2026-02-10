FROM python:3.10-slim

WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/app.py .

ENV APP_VERSION=v1
ENV APP_MESSAGE=local-default
ENV FEATURE_FLAG=off

EXPOSE 8080
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
