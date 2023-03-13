from django.urls import path
from .views import index, produto, carrinho, base

urlpatterns = [
    path('', index , name='home'),
    path('produto', produto, name='produtos'),
    path('produto/carrinho', carrinho, name='carrinho'),
    path('b', base, name='b')
]