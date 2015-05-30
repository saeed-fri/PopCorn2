from django import forms
from User.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    alias = forms.CharField(required=True)
    password = forms.CharField(required=True)
    confPassword = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    birthday = forms.DateTimeField(required=True)

"""
blog = models.ForeignKey(Blog)
name = models.CharField(max_length=100)
comment = models.TextField()
timestamp = models.DateTimeField(default=datetime.datetime.now)
"""
class RegisterModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'alias', 'password', 'email', 'birthday']
