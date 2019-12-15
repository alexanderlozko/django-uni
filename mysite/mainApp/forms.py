from django import forms
from .models import Comment, Order, BackCall

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'comment')

class BackCallForm(forms.ModelForm):
    class Meta:
        model = BackCall
        fields = ('name', 'phone', 'email', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'myfieldclass'}),
            'phone':forms.NumberInput(attrs={"class":"form-group"}),
            'email':forms.EmailInput(attrs={"class":"form-group"}),
            'message':forms.Textarea(attrs={"class":"form-group-2 mb-4"}),
            }

class OrderOnlineForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'phone', 'email', 'category', 'message', 'files')