# Python бейнесі негізінде контейнер құрамыз
FROM python:3.11-slim

# Жұмыс қалтасы
WORKDIR /app

# Тәуелділіктерді орнату
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Қолданбаның барлық файлдарын көшіру
COPY . .

# Порт 5000 ашу
EXPOSE 5000

# Қосымшаны Gunicorn арқылы іске қосу
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app", "--workers", "2"]