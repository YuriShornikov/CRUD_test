#django-admin startproject lesson1 .    - создание своего проекта lesson1(название)  . - место создания, в данном случае это расположение место папки
#python manage.py runserver - запуск сервера
#./manage.py migrate - создание бд
#python manage.py startapp demo   запуск приложения с названием demo
#ctrl-Breake   - остановка работы сервера
#в созданном пакете через app в файле views.py прописывают функции для пользователя
#в пакете lesson1 в файле urls.py прописываются связи с views.py для отображения для пользователя в браузере (роутинг)
#python manage.py makemigrations в папке migrations создается файл с записями изменений
#python manage.py migrate - чтобы вступили в силу изменения
#python manage.py createsuperuser создание админки
#admin dbonlyfun@gmail.com Irregularlydgango
# views     models       urls     templates
#creatdb -U postgres (название бд)
#pip install psycopg2-binary
#pip install django_filter   в  settings INSTALLED_APPS прописываем 'django_filters', а так же для использования
#REST_FRAMEWORK = {
    #'DEFAULT_FILTER_BACKEND': [
        #'django.filters.rest_framework.DjangoFilterBackend'
    #]
#}