from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import main_view
from .views import chat_view

app_name = 'main'

urlpatterns = [
    path('', main_view, name='main_view'),
    path('chat/<int:receiver>', chat_view, name='chat_view'),
    path('logout/', LogoutView.as_view(), name='logout_view'),
]

