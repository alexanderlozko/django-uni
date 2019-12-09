from django import forms
from .models import Comment, Order, BackCall

class RegisterForm(forms.Form):
    email = forms.EmailField()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'comment')

class BackCallForm(forms.ModelForm):
    class Meta:
        model = BackCall
        fields = ('name', 'phone', 'email', 'message')

class OrderOnlineForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'phone', 'email', 'category', 'message', 'files')