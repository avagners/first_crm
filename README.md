# Frist_CRM

### Описание
> Pet-проект для закрепления навыков по работе с Django и DRF.

First_CRM - это crm-система для автоматизированного взаимодействия с клиентами и ведения учета малого бизнеса в сфере услуг.
![screen](/first_crm/static/img/Screenshot.png)
### Технологии
- Django 4.0.3

## Запуск проекта в dev-режиме
Клонировать репозиторий и перейти в него в командной строке:

    git clone git@github.com:avagners/first_crm.git
    cd first_crm

Cоздать и активировать виртуальное окружение:

    python3 -m venv venv
    source venv/bin/activate

Установить зависимости из файла requirements.txt:

    python3 -m pip install --upgrade pip
    pip install -r requirements.txt

Выполнить миграции:

    python3 manage.py makemigrations
    python3 manage.py migrate

В папке с файлом manage.py выполните команду:

    python3 manage.py runserver
