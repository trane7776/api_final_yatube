# Yatube API

API сервис для социальной сети Yatube. Позволяет публиковать записи, комментировать их и подписываться на других авторов.

## Функциональность

- Публикация записей
- Комментирование записей
- Группы для записей
- Подписка на авторов
- JWT-аутентификация
- Получение, создание, обновление и удаление записей
- Работа с изображениями

## Технологии

- Python 3.7+
- Django 2.2.16
- Django REST Framework
- Simple JWT

## Как запустить проект

Клонировать репозиторий и перейти в него:

```bash
git clone https://github.com/your_username/api_final_yatube.git
cd api_final_yatube
```

Создать и активировать виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate  # для Linux/macOS
source venv/Scripts/activate  # для Windows
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

Выполнить миграции:

```bash
python manage.py migrate
```

Запустить проект:

```bash
python manage.py runserver
```

## Примеры API запросов

### Получение публикаций

```
GET /api/v1/posts/
```

### Создание публикации

```
POST /api/v1/posts/

{
    "text": "Текст публикации",
    "image": "string",
    "group": 0
}
```

### Получение JWT-токена

```
POST /api/v1/jwt/create/

{
    "username": "string",
    "password": "string"
}
```

## Документация API

Полная документация API доступна по адресу `http://127.0.0.1:8000/redoc/` после запуска проекта.

## Автор

Ваше имя

## Лицензия

MIT
