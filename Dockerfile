# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем зависимости
RUN pip install pandas

# Копируем файлы проекта
COPY app.py /app.py
COPY data.csv /data.csv

# Устанавливаем рабочую директорию
WORKDIR /

# Запускаем приложение
CMD ["python", "app.py"]
