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
