from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserCreationForm
from .forms import UserChangeForm

from .models import Message
from .models import Account

class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm

    list_display = ('email', 'username', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'creation_date')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'username', 'password1', 'password2', 'creation_date',
                'is_active', 'is_staff', 'is_superuser'),
        }),
    )
    search_fields = ('username',)
    ordering = ('creation_date',)
    filter_horizontal = ()


admin.site.register(Account, UserAdmin)
admin.site.register(Message)
admin.site.unregister(Group)

# Register your models here.
