# Отчёт по домашней работе №4

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

## Работа с ветками

- `hw1` - Домашнее задание №1
- `hw2` - Домашнее задание №2
- `hw3` - Домашнее задание №3
- `hw4` - **Домашнее задание №4**
- `hw5` - Домашнее задание №5
- `hw6` - Домашнее задание №6


## Запуск окружения
```bash
uv venv

uv sync
```


ДЗ - Автоматизация ML пайплайнов
Описание
Создайте автоматизированные ML пайплайны с использованием
современных инструментов оркестрации.
Требования
Выберите ОДИН из инструментов для оркестрации пайплайнов:
- Snakemake - Workflow management system
- DVC Pipelines - Data versioning pipelines
- Apache Airflow - Workflow orchestration platform
- Luigi - Python workflow management
Выберите ОДИН из инструментов для управления конфигурациями:
- Hydra - Configuration management framework
- OmegaConf - YAML configuration library
- Pydantic - Data validation and settings
1. Настройка выбранного инструмента оркестрации:
   - Установить и настроить выбранный инструмент
   - Создать workflow для ML пайплайна
   - Настроить зависимости между этапами
   - Реализовать кэширование и параллельное выполнение
2. Настройка выбранного инструмента конфигураций:
   - Настроить выбранный инструмент для управления
   - конфигурациями
   - Создать конфигурации для разных алгоритмов
   - Настроить валидацию конфигураций
   - Создать систему композиции конфигураций
3. Интеграция и тестирование:
   - Интегрировать выбранные инструменты
   - Создать систему мониторинга выполнения
   - Настроить уведомления о результатах
   - Протестировать воспроизводимость
4. Отчет о проделанной работе:
   - Создать отчет в формате Markdown
   - Описать настройку выбранных инструментов
   - Добавить скриншоты результатов
   - Сохранить отчет в Git репозитории


```
engineering-practices-ml
├─ .dvc
│  ├─ cache
│  │  └─ files
│  │     └─ md5
│  │        ├─ 1b
│  │        ├─ 3e
│  │        ├─ 44
│  │        └─ 71
│  └─ tmp
├─ .pre-commit-config.yaml
├─ classification_module
│  ├─ config.py
│  ├─ dataset.py
│  ├─ features.py
│  ├─ modeling
│  │  ├─ predict.py
│  │  ├─ train.py
│  │  └─ __init__.py
│  ├─ plots.py
│  └─ __init__.py
├─ Dockerfile
├─ docs
│  ├─ docs
│  │  ├─ getting-started.md
│  │  └─ index.md
│  ├─ mkdocs.yml
│  └─ README.md
├─ Makefile
├─ models
├─ notebooks
├─ pyproject.toml
├─ README.md
├─ references
├─ reports
│  └─ figures
│     └─ jupyter_lab.png
├─ requirements.txt
└─ uv.lock

```
