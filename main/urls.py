from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import main_view

app_name = 'main'

urlpatterns = [
    path('', main_view, name='main_view'),
    path('logout/', LogoutView.as_view(), name='logout_view'),
]

