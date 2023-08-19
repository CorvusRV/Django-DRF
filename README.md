# Django/DRF приложение

    Это небольшое приложение для регистрации пользователей по номеру телефона.

## Работа приложения

    Для работы приложения вам необходимо создать .env файл и внести в него три параметра:
        PG_NAME = '<value>' - название базы данных
        PG_USER = '<value>' - имя пользователя
        PG_PASSWORD = '<value>' - пароль
        
    Так же можно разкоментировать данные для работы через SQLite и закоментировать данные для работы через PostgreSQL

    Рекомендуется перед работай с API создать суперпользователя, его id будет 1

# REST API

    API REST для примера работы приложения.

## Получить список пользователей

### Запрос

`GET /users/`

    curl -i -H 'Accept: application/json' http://localhost:8000/users/

### Ответ

    [{"id":1,"phone":"11111111111","user_code":"123456","invite_code""}]

## Авторизация(Регистрация) пользователя

### Запрос

`POST /users/`

    curl -i -H 'Accept: application/json' -d '&phone=88008008080' http://localhost:8000/users

### Ответ

    {"phone":"88008008080","sms_code":8000}

### Запрос 2 (с полученным смс кодом)

`POST /users/`

    curl -i -H 'Accept: application/json' -d '&phone=88008008080,&code=8000' http://localhost:8000/users

### Ответ

    {"token": "(<Token: 0000000000000000000000000000000000000000>, True)"}
    В ответ приходит токен авторизации пользователя

## Получить информации о пользователе

### Запрос

`GET /users/id`

    curl -i -H 'Accept: application/json' http://localhost:8000/users/2

### Ответ

    {"id":2,"phone":"88008008080","user_code":"800800","invite_code"","invited_users":[]}

## Получить информации о несуществующем пользователе

### Запрос

`GET /users/id`

    curl -i -H 'Accept: application/json' http://localhost:8000/users/9999

### Ответ

    {"status":404,"reason":"Not found"}

## Регистрация нового пользователя

### Запрос

`POST /users/`

    curl -i -H 'Accept: application/json' -d '&phone=99009009090' http://localhost:8000/users

### Ответ

    {"phone":"99009009090","sms_code":1111}

## Получить информации о новом пользователе

### Запрос

`GET /users/id`

    curl -i -H 'Accept: application/json' http://localhost:8000/users/3

### Ответ

    {"id":3,"phone":"99009009090","user_code":"1+1900","invite_code"","invited_users":[]}

## Добавить инфайт код пользователю

### Запрос

`PATCH /users/id`

    curl -i -H 'Accept: application/json' -d '&invite_code=1+1900' -X PATCH http://localhost:8000/users/2

### Ответ

    {"id":2,"phone":"88008008080","user_code":"800800","invite_code"1+1900","invited_users":[]}

## Получить информации о новом пользователе

### Запрос

`GET /users/id`

    curl -i -H 'Accept: application/json' http://localhost:8000/users/3

### Ответ

    {"id":3,"phone":"99009009090","user_code":"1+1900","invite_code"","invited_users":[88008008080]}

## Получить список пользователей

### Запрос

`GET /users/`

    curl -i -H 'Accept: application/json' http://localhost:8000/users/

### Ответ

    [{"id":1,"phone":"11111111111","user_code":"123456","invite_code""},{"id":2,"phone":"88008008080","user_code":"800800","invite_code"1+1900"},{"id":3,"phone":"99009009090","user_code":"1+1900","invite_code"}]

## Изменить инфайт код пользователю

### Запрос

`PATCH /users/id`

    curl -i -H 'Accept: application/json' -d '&invite_code=111111' -X PATCH http://localhost:8000/users/2

### Ответ

    {"id":2,"phone":"88008008080","user_code":"800800","invite_code"1+1900","invited_users":[]}
