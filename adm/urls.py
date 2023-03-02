from django.urls import path
from .views import index, error404, login, register, forgot_password, blank, form, registros, teste

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('forgot_password', forgot_password, name='forgot_password'),
    path('error404', error404, name='error404'), 
    path('blank', blank, name='blank'),
    path('form', form, name='form'),
    path('registros', registros, name='registros'),
    path('teste', teste, name='teste')
]