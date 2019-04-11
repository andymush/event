from django import forms
from .models import Comment
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['email', 'comment']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
