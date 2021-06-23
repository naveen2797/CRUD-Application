from django import forms
from django.forms import widgets
from .models import User




class studentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','contact','password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'contact': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'})
        }
       