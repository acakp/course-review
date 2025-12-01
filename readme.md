# Установка

1. Установите Python 3.10+
2. Создайте виртуальное окружение:
```
python -m venv venv
source venv/bin/activate
```
3. Установите зависимости:
```
pip install -r requirements.txt
```
4. Установите PostgreSQL и создайте там БД, которую будете использовать
5. Создайте .env файл с необходимыми данными для входа (пример в .env.dist)
6. Миграции:
```
python manage.py migrate
```
7. Запуск:
```
python manage.py runserver
```

**Готово — сайт доступен на:**
```
http://127.0.0.1:8000
```



## activate venv in fish shell:

```
  source venv/bin/activate.fish
```

для запуска сервера:
```
   python coursereview/manage.py runserver
```
или, если вы хотите запустить сервер без активации, вы можете явно указать путь к python: `venv/bin/python ` вместо `python`

## Посмотреть последние 5 добавленных записей:

1. Подключиться к django shell:
```
  python coursereview/manage.py shell
```
2. Импортировать нужную модель (например Course):
```
  from review_app.models import Course
```
3. Вывести последние 5 записей:
```
  Course.objects.order_by('-id')[:5]
```
