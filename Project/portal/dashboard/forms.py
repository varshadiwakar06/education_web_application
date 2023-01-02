from django import forms
from django.forms import widgets
from.models import *
from django.contrib.auth.forms import UserCreationForm

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title','description']

class DashboardForm(forms.Form):
    text = forms.CharField(max_length=100,label="Please search here : ")

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','is_finished']


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']