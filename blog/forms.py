from django import forms
from django.contrib.auth.models import User
from .models import Post, UserProfile
from material import Layout, Row, Column, Fieldset, Span2, Span3, Span5, Span6, Span10

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    layout = Layout('username', 'password')

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'pinned_post',) 

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    layout = Layout('username', 'password', 'email')

    class Meta:
        model = User
        fields = ('username', 'password', 'email',)

class UserProfileForm(forms.ModelForm):

    layout = Layout('description', 'picture', 'website',)

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['picture'].label = "Attach a profile picture..."

    class Meta:
        model = UserProfile
        fields = ('description', 'picture', 'website',)
