FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Убедитесь, что gunicorn есть в requirements.txt
RUN pip install gunicorn

COPY . .

CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8080"]
