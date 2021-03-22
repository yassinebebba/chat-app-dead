from django.shortcuts import render
from django.shortcuts import reverse
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from datetime import datetime
from .forms import CustomLoginForm


class CustomLoginView(SuccessMessageMixin, LoginView):
    template_name = 'authentication/login.html'

    # this needs extra methods
    # form_class = CustomLoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['body_class'] = 'start'
        return context

    def get_success_url(self):
        return reverse('authentication:main:main_view', )

    def get_success_message(self, cleaned_data):
        date = datetime.now().hour
        if 5 <= date <= 11:
            return f'Good morning, {self.request.user.username}.'
        elif 12 <= date <= 17:
            return f'Good afternoon, {self.request.user.username}.'
        else:
            return f'Good evening, {self.request.user.username}.'


def login_view(request):
    return render(request, 'authentication/login.html', context={'body_class': 'start'})


def sign_up_view(request):
    return render(request, 'authentication/sign_up.html', context={'body_class': 'start'})
