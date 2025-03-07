FROM python:3.9-slim

WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код после установки зависимостей
COPY . .

# Указываем порт, который будет использоваться
EXPOSE 8080

# Запускаем сервер Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app.wsgi:application"]
