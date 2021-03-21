from django.shortcuts import render


def login_view(request):
    return render(request, 'authentication/login.html', context={'body_class': 'start'})

def sign_up_view(request):
    return render(request, 'authentication/sign_up.html', context={'body_class': 'start'})
