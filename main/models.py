from django.db import models

from django.utils import timezone
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import _user_has_perm
from django.contrib.auth.models import _user_has_module_perms
from django.core.exceptions import ObjectDoesNotExist


class AccountManager(BaseUserManager):
    def create_user(self, email, username, password):
        if not email:
            raise ValueError('User must have an email.')
        if not username:
            raise ValueError('User must have a username.')
        if not password:
            raise ValueError('User must have a password.')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=email,
            username=username,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractUser):
    email = models.EmailField(max_length=255, unique=True, null=False)
    username = models.CharField(max_length=30, unique=True, null=False)
    creation_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def has_perm(self, perm, obj=None):
        if self.is_active and self.is_superuser:
            return True
        return _user_has_perm(self, perm, obj)

    def has_perms(self, perm_list, obj=None):
        return all(self.has_perm(perm, obj) for perm in perm_list)

    def has_module_perms(self, app_label):
        if self.is_active and self.is_superuser:
            return True

        return _user_has_module_perms(self, app_label)

    def __str__(self):
        return f'{self.username} -> {self.email}'

class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, null=False)
    profile_picture = models.ImageField(upload_to='profile_pictures', default='c++.png')


    def __str__(self):
        return f'{self.user.username}'


class Friend(models.Model):
    user = models.ForeignKey(Account, related_name='user_set', on_delete=models.CASCADE, null=False)
    friend = models.ForeignKey(Account, related_name='friend_set', on_delete=models.CASCADE, null=False)

    def check_friend(self, user, friend):
        try:
            if Friend.objects.get(user=user, friend=friend):
                return True
        except ObjectDoesNotExist:
            return False

    def __str__(self):
        return f'{self.user.username} is friends with {self.friend.username}'


class Message(models.Model):
    sender = models.ForeignKey(Account, related_name='sender_set', on_delete=models.DO_NOTHING, null=False)
    receiver = models.ForeignKey(Account, related_name='receiver_set', on_delete=models.DO_NOTHING, null=False)
    msg_body = models.CharField(max_length=250, null=False)
    # file = models.FileField()
    creation_date = models.DateTimeField(auto_now=True, null=False)
    read = models.BooleanField(default=False, null=False)
    deleted = models.BooleanField(default=False, null=False)
    

    def __str__(self):
        return f'{self.sender} ({self.creation_date})-> {self.receiver}'
