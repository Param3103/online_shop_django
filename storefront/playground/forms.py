from django import forms
from .models import user
import time
class LoginForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ("name", "age")