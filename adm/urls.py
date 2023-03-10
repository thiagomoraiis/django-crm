from django.urls import path
# from .views import dashboard, error404, login, register, forgot_password, blank, form, registros, edit, deletar , solicitacoes
from .views import solicitar
from .views import *

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('forgot_password', forgot_password, name='forgot_password'),
    path('error404', error404, name='error404'), 
    path('blank', blank, name='blank'),
    path('form/', form, name='form'),
    path('registros/', registros, name='registros'),
    path('edit/<int:id>/', edit, name='edit'),
    path('deletar/<int:id>/', deletar, name='deletar'),
    path('solicitacoes/', solicitacoes, name='solicitacoes'),
    path('solicitar', solicitar, name='solicitar'),
    path('edit_solicitar/<int:id>/', edit_solicitar, name='edit_solicitar'),
    path('del_solicitar/<int:id>/', del_solicitar, name='del_solicitar'),
    # path('teste/', teste, name='teste')
]