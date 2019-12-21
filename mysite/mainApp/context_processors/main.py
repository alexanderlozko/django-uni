from mysite.mainApp.models import Comment, BackCall
from django.template.context_processors import request

def comments(request):
    comments = Comment.objects.filter(published=True).order_by('-datetime')
    amount = BackCall.objects.count()
    return {'comments':comments, 'amount':amount}