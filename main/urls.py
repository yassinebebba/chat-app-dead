from django.urls import path
from django.urls import include

from .views import main_view

app_name = 'main'

urlpatterns = [
    path('', main_view, name='main_view'),
]
