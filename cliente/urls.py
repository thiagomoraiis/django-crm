from django.urls import path
from .views import index, produto

urlpatterns = [
    path('', index , name='home'),
    path('produto', produto, name='produtos'),
]