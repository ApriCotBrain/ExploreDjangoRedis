## ExploreDjangoRedis

### Цель данного проекта - изучение кэширования в базе данных Redis в рамках Django проекта. В проекте будут рассмотрены следующие задачи:  установка Redis, интеграция Redis в Django, создание кэшей и их использование на примере кэширования JWT-токенов.

### Используемые техологии:
- Django==4.2.1
- django-redis==5.2.0
- djangorestframework==3.14.0
- djangorestframework-simplejwt==4.7.2
- djoser==2.1.0
- сервер Redis

### Как запустить проект:
- Установите сервер Redis https://redis.io/docs/getting-started/installation/
- Склонируйте проект git clone git@github.com:ApriCotBrain/ExploreDjangoRedis.git
- Создайте и активируйте виртуальное окружение, перейдите в папку с проектом cd django_cache/ и установите зависимости:

```python -m venv venv```

```source venv/Scripts/activate```

```pip install -r requirements.txt```
- Примените миграции:

```python manage.py migrate```

- Создайте суперпользователя, запустите сервер:

```python manage.py createsuperuser```

```python manage.py runserver```

### Что сделано:
- Добавлена конфигурация кэширования в настройках проекта с использованием Redis в качестве кэш-бэкенда
- Написаны функции кэширования токенов в utils.py 
- Добавлены эндпоинты и представления для кэширования токенов

### Как протестировать:
- Получите токен в Postman http://127.0.0.1:8000/api/auth/jwt/create/
```
{
"username": "myname",
"password": "mypassword"
}
```
-  Сохраните токен в Redis http://127.0.0.1:8000/api/set_jwt_token/
```
{
  "token": "mytoken",
  "user_id": 1
}
```
Получите пользователя по токену http://127.0.0.1:8000/api/get_user_id_from_jwt_token/
```
{
  "token": "mytoken",
}
```
- Увидеть какие ключи сохранены на Redis сервере можно по команде KEYS *

### TODO: 
- Подумать как протестировать временную разницу в приложении с использованием кэша и без
