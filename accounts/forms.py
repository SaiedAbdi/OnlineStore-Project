from django import forms
from django.forms.widgets import Widget
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from accounts import models

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email','full_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise forms.ValidationError('passwords must match')
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email','password','full_name')

    def clean_password(self):
        return self.initial['password']



class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Email ',widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))


class UserRegisterForm(forms.Form):
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Your Email Here'}))
    full_name = forms.CharField(label='User name', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Username Here'}))
    password1 = forms.CharField(label = 'Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password Here'}))
    password2 = forms.CharField(label = 'Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password here'}))

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords must match')
        return cd['password2']
        