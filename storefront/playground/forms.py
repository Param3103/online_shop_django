from django import forms
from .models import User
import time
class LoginForm(forms.ModelForm):
    name=forms.CharField()
    age=forms.IntegerField()
    class Meta:
        model = User
        fields = ("name", "age",)