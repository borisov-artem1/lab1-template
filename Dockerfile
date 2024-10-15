# Используем официальный Python-образ
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы с зависимостями
COPY djangoProject/requirements.txt /app/requirements.txt

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копируем исходный код в контейнер
COPY . /app/

# Открываем порт для приложения
EXPOSE 8080

# Выполняем миграции, собираем статику и запускаем сервер
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:8080"]
