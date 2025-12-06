#!/bin/bash
set -e

# Запускаем MLflow в фоне
mlflow server \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root ./mlruns \
  --host 0.0.0.0 \
  --port 5000 &

# Запускаем JupyterLab в foreground (чтобы контейнер не завершился)
jupyter lab --ip=0.0.0.0 --port=8888 --allow-root
