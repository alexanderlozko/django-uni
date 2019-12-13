import simplejson as simplejson
from django.http import HttpResponseRedirect, JsonResponse, Http404, HttpResponse
from django.shortcuts import render
from django.urls import reverse
import requests
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer

from .forms import CommentForm, BackCallForm, RegisterForm
from .models import Comment, BackCall, Order, Category
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import CommentSerializer

class CommentView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response({"comments": serializer.data})

def index(request):
    comments = Comment.objects.filter(published=True).order_by('-datetime')
    amount = Comment.objects.filter(published=True).count()

    return render(request, 'index.html', {'comments':comments, 'amount': amount})


def add_ajax(request):
    if request.is_ajax():
        first_text = 'Оценка жилой/коммерческой недвижимости'
        second_text = 'Оценка товаров в обороте'
        third_text = 'Оценка транпортных средств'

        response = {'first-text': first_text,
                    'second-text': second_text,
                    'third-text': third_text}

        return JsonResponse(response)
    else:
        raise Http404

def add_comment(request):
    if request.is_ajax():
        comments = Comment.objects.filter(published=True)[::1]
        more_comments = CommentSerializer(comments, many=True)
        response = {'more_comments': more_comments.data}

        return Response(response)
    else:
        raise Http404

class CommentsDetail(generics.RetrieveAPIView):
     renderer_classes = [TemplateHTMLRenderer]
     template_name = 'comments.html'

     def get(self, request):
         queryset = Comment.objects.filter(published=True)[::1]
         return Response({'comments': queryset})


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
    response = requests.get('http://api.ipstack.com/check?access_key=5f76bbb6c812076967c64cbde6084147')
    geodata = response.json()
    return render(request, 'registration/profile.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })

def service(request):
    return render(request, 'service.html')

def order_online(request):
    return render(request, 'order_online.html')
