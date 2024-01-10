# last_course_in_lesson

Что бы запустить нужно:
   1. открыть терминал
   2. написать туда вот это: celery -A project worker --loglevel=info
   3. открыть второй терминал
   4. написать туда вот это: celery -A project beat --loglevel=info
   5. открыть третий терминал
   6. написать туда вот это: python manage.py runserver
   7. зайти на URL, зарегистрироватся: http://127.0.0.1:8000/users/register/ или авторизаватся: http://127.0.0.1:8000/users/login
   8. зайти на свой профиль и указать Chat id
      по этому URL: http://127.0.0.1:8000/users/profile/
   9. зайти на страницу создание превычек и создать ее
      по этому URL: http://127.0.0.1:8000/costumbre/create/
   10 если хотите можете посмотреть все или одну превичку
      по этому URL можете посмотреть одну привычку: http://127.0.0.1:8000/costumbre/id вашей привички/
      по этому URL можете посмотреть все привычки: http://127.0.0.1:8000/costumbre/


Где взять Chat id: нужно зайти в телеграмм каннал: https://t.me/userinfobot и написать /start вам ответят виде столбца и ID это и есть Chat id

пример:
   @ваш ник
   Id: ваш chat_id
   First: ваша ник
   Lang: ru

docker:
1. docker build -t hello .
2. docker run --name test_cont -d -p 8000:8000 hello


docker-compose
1. docker-compose build
2. docker-compose up