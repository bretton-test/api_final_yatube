# api_final
# API для проекта Yatube

## 1. [Описание](#1)
## 2. [Команды для запуска](#2)
## 3. [Доступные эндпоинты](#3)
## 4. [Примеры запросов](#4)


---
## 1. Описание <a id=1></a>

Проект API для социальной сети [Yatube](https://github.com/bretton-test/api_final_yatube).  
Позволяет создавать, читать, изменять и удалять свои посты, а так же читать чужие посты и подписываться на их авторов посредством API-запросов.  
Для неавторизованных пользователей API доступен только для чтения.

---
## 2. Команды для запуска <a id=2></a>

Перед запуском необходимо склонировать проект:
```bash
HTTPS: git clone git@github.com:bretton-test/api_final_yatube.git
```

Cоздать и активировать виртуальное окружение:
```bash
python -m venv venv
```
```bash
Windows: source venv/Scripts/activate
```

И установить зависимости из файла requirements.txt:
```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Выполнить миграции:
```bash
python manage.py migrate
```
Добавить администратора
```bash
python manage.py createsuperuser
```

Запустить проект:
```bash
python manage.py runserver
```


Теперь доступность проекта можно проверить по адресу [127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---
## 3. Доступные эндпоинты <a id=3></a>

Посты:
```
"/api/v1/posts/" (Параметры для фильтрации "?limit=0&offset=0"),
"/api/v1/posts/{id}/"
```

Группы:
```
"/api/v1/groups/",
"/api/v1/groups/{id}/"
```

Комментарии:
```
"/api/v1/posts/{id}/comments/",
"/api/v1/posts/{id}/comments/{id}/"
```

Подписки (Только для авторизованных пользователей):
```
"/api/v1/follow/" (Параметр для поиска "?search=''")
```

Получение токена для доступа к API (Для зарегистрированных пользователей):
Post ("username": "string","password": "string")
```
"/api/v1/auth/jwt/create/"
```
Обновление JWT-токена. Post ("refresh": "string" required)
```
"/api/v1/jwt/refresh/"
```
Проверка JWT-токена. Post ("token": "string")
```
"/api/v1/jwt/verify/"
```
---
## 4. Примеры запросов <a id=4></a>

Получение списка всех постов:
```
Method: GET
Endpoint: "/api/v1/posts/"
```

Публикация поста:
```
Method: POST
Endpoint: "/api/v1/posts/"
Payload:
{
    "text": "string",
    "image": "string",
    "group": 0
}
```

Получение JWT-токена:
```
Method: POST
Endpoint: "/api/v1/auth/jwt/create/"
Payload:
{
    "username": "string",
    "password": "string"
}
```

---
