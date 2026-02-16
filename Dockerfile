# Облегчённый вариант питона
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Убираем логи и pycache
ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Копируем все зависимости
COPY requirements.txt .

# Запускаем питон и подтягиваем зависимости, без кэша
RUN pip install --no-cache-dir -r requirements.txt

# Теперь копируем весь проект
COPY . .

# Команда для запуска бота
CMD ["python", "main.py"]