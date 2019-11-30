from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import CommentForm, BackCallForm
from .models import Comment, BackCall, Order


def index(request):
    comments = Comment.objects.filter(published=True).order_by('-datetime')
    amount = Comment.objects.filter(published=True).count()

    return render(request, 'index.html', {'comments':comments, 'amount': amount})

def aboutus(request):
    return render(request, 'about.html')

def contact(request):
    sent = False
    if request.method == 'POST':
        form = BackCallForm(request.POST)
        if form.is_valid():
            sent = True
            form.save()
    else:
        form = BackCallForm()
    return render(request, 'contact.html', {'form': form, 'sent': sent})

def comment(request):
    sent = False
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            sent = True
            form.save()

    else:
        form = CommentForm()
    return render(request, 'comment.html', {'form': form, 'sent':sent})

def profile(request):
    return render(request, 'registration/profile.html')

def service(request):
    return render(request, 'service.html')

def order_online(request):
    return render(request, 'order_online.html')