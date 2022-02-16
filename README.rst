Как настроить окружение?
- Проверить pyenv --version
-- Если ошибка - установить pyenv по инструкции https://realpython.com/intro-to-pyenv/
-- Повторно проверить pyenv --version
- Установить pyenv install -v 3.9.6
- Включаем pyenv local 3.9.6
- Устанавливаем окружение pipenv install

Как запустить окружение?
- Выполнить в корне проекта pipenv shell

Как подготовиться к запуску БД?
- Проверить, что установлен docker - docker --version
- Если не установлен docker - установить по инструкции https://docs.docker.com/engine/install/.
Выбрать конкретный раздел в зависимости от вашей ОС
- Проверить, что установлен docker-compose - docker-compose --version
- Если не установлен docker-compose - установить по инструкции https://docs.docker.com/compose/install/

Как запустить БД?
- Выполнить в корне проекта docker-compose up -d
- Выполнить docker ps и убедиться, что запущен контейнер с postgresql на порту 7432

Как выполнить миграции приложения?
- Перейти в директорию intensive
- Выполнить python manage.py migrate

Как запустить приложение?
- Перейти в директорию intensive
- Выполнить python manage.py runserver
- Перейти в браузер на страницу http://127.0.0.1:8000/ и убедиться, что открылась стартовая страница

