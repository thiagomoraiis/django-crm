from django.urls import path
from .views import dashboard, error404, login, register, forgot_password, blank, form, registros, edit, deletar , solicitacoes, teste
# from .views import criar_solicitacao

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
    # path('solicitar', criar_solicatacao, name='solicitar'),
    path('teste/', teste, name='teste')
]