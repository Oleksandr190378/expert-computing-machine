FROM python:3.11.7

# Встановимо змінну середовища
ENV APP_HOM /assistant

# Встановимо робочу директорію всередині контейнера
WORKDIR $APP_HOM

COPY pyproject.toml  $APP_HOM/pyproject.toml
COPY poetry.lock  $APP_HOM/poetry.lock

# Встановимо залежності всередині контейнера
RUN pip install poetry
RUN poetry config virtualenvs.create false 
RUN poetry install --only main

# Скопіюємо інші файли в робочу директорію контейнера
COPY . .

# Запустимо наш застосунок всередині контейнера
ENTRYPOINT ["python", "main.py"]