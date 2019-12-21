from django import forms
from .models import Comment, Order, BackCall

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Имя'}),
            'message': forms.Textarea(attrs={'class':'form-control', 'rows':'4', 'placeholder':'Ваш комментарий'}),
        }

class BackCallForm(forms.ModelForm):
    class Meta:
        model = BackCall
        fields = ('name', 'phone', 'email', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Имя'}),
            'phone':forms.NumberInput(attrs={'type':"tel", 'class':'form-control', 'placeholder':"Телефон (+380)" , 'pattern':"[\+][3][8][0]\d{9}", 'minlength':"13", 'maxlength':"13"}),
            'email':forms.EmailInput(attrs={'type':"email", 'class':"form-control", 'placeholder':"Почта"}),
            'message':forms.Textarea(attrs={'class':'form-control', 'rows':'4', 'placeholder':'Ваше сообщение '}),
            }

class OrderOnlineForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'phone', 'email',  'message')