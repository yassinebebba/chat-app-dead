from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models import QuerySet

from .models import Friend
from .models import Account
from .models import Message


@login_required()
def main_view(request):
    friends = Friend.objects.filter(user=request.user)
    context = {
        'friends': friends,
        'msgs': request.user.sender_set.all()
    }
    return render(request, 'main/main_app.html', context=context)


@login_required()
def chat_view(request, receiver):
    print("#####################")
    print(request.user.sender_set.all())
    print("#####################")
    friends = Friend.objects.filter(user=request.user)
    a = request.user
    b = Account.objects.get(pk=receiver)

    msgs = Message.objects.filter(
        ((Q(sender=a) & Q(receiver=b)) | (Q(sender=b) & Q(receiver=a))))
    msgs = QuerySet.order_by(msgs, 'creation_date')
    context = {
        'friends': friends,
        'msgs': msgs,
        'current_chat': b
    }
    return render(request, 'main/chat.html', context=context)
