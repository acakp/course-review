## activate venv in fish shell:

```
  source venv/bin/activate.fish
```

to start the server:
```
   python coursereview/manage.py runserver
```
or, if you want to run server without activation, you can explicitly specify python path: `venv/bin/python `instead of `python` 

django admin panel credentials:
user: `bunny`
password: `admin`

postgresql db credentials:
db name: `course_review`
pwd: `blind`

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
