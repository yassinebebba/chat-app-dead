from django.urls import path
from django.urls import include

from .views import login_view
from .views import sign_up_view

app_name = 'authentication'

urlpatterns = [
    path('', login_view, name='login_view'),
    path('singup/', sign_up_view, name='sign_up_view'),
    path('app/', include('main.urls'))
]
