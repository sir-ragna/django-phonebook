
Init venv environment

    [robbe@teslacoil django_tut]$ python -m venv venv
    [robbe@teslacoil django_tut]$ source venv/bin/activate

- Install django
- Create a new project with django-admin
- run server `cd tutorial1 && python manage.py runserver`

- Create another app
  - mkdir phonebook
  - create urls.py
  - create views.py
  - create models.py
    - Create `PhoneRecord` model

Do the migrations

    python manage.py makemigrations phonebook
    python manage.py migrate
    python manage.py migrate


Initially create a form with bootstrap in `new_record.html`.
To be replaced with the automatic _form_ generation of Django.