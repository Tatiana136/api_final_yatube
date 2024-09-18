### API сервис для социальной сети Yatube.

## Реализация

- Аутентификация построена на JWT-токенах
- Неаутентифицированные пользователи имеют ограниченный доступ. Только чтение.
- Аутентифицированным пользователям разрешается удаление и изменение только своего контента.
- Создание, изменение, удаление постов и комментариев.
- Реализация подписки на другого пользователя.

# Документация: [ReDoc](http://127.0.0.1:8000/redoc/)

## Как запустить проект

**Клонировать репозиторий и перейти в него в командной строке:**
git clone <название репозитория>
cd api_final_yatube

**Cоздать и активировать виртуальное окружение:**
python3 -m venv api
source api/bin/activate

**Установить зависимости из файла requirements.txt:**
python3 -m pip install --upgrade pip
pip install -r requirements.txt

**Выполнить миграции:**
python3 manage.py migrate

**Запустить проект:**
python3 manage.py runserver

## Примеры запросов

**Получить список всех постов:** GET api/v1/posts/

**Создание публикации:** POST api/v1/posts/

**Удаление публикации:** DELETE api/v1/posts/{id}/

**Получение комментариев:** GET api/v1/posts/{post_id}/comments/

**Удаление комментария:** DELETE api/v1/posts/{post_id}/comments/{id}/

**Список сообществ:** GET api/v1/groups/

**Подписка пользователя, от имени которого сделан запрос:** POST api/v1/follow/