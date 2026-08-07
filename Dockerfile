FROM demisto/fastapi:0.125.0.11206988

COPY . /app

WORKDIR /app

EXPOSE 8000

RUN pip install --no-cache-dir -r requirements.txt

# Запускаем FastAPI приложение
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]