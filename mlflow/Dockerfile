FROM python:3.11-slim

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

# Запуск MLflow сервера (или обучения)
EXPOSE 5000

CMD ["mlflow", "server", \
     "--backend-store-uri", "sqlite:///mlflow.db", \
     "--default-artifact-root", "./mlruns", \
     "--host", "0.0.0.0", \
     "--port", "5000"]
