from django import forms
from .models import Password

class PasswordForm(forms.Form):
    text = forms.CharField()

    class Meta:
        model = Password
        fields = ('text',)