from mysite.mainApp.models import Comment
from django.template.context_processors import request

def comments(request):
    comments = Comment.objects.filter(published=True).order_by('-datetime')
    amount = Comment.objects.count()
    return {'comments':comments, 'amount':amount}