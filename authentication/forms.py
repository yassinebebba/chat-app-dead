from django import forms
from main.models import Account

class CustomLoginForm(forms.ModelForm):

    """ work in progress """

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CustomLoginForm, self).__init__(*args, **kwargs)

    email = forms.CharField(max_length=250, required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ['email', 'password',]


    def is_valid(self):
        pass

    def get_user(self):
        pass

