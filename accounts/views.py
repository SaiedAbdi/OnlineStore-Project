from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import User

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            user= authenticate(request,email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request,'you logged in successfully', 'success')
                return redirect('shop:home')
            else:
                messages.error(request, 'username or password is wrong', 'danger')

    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form':form})

def user_logout(request):
    logout(request)
    messages.success(request,'you loged out successfully', 'success')
    return redirect('shop:home')

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['email'], cd['full_name'], cd['password2'])
            user.save()
            messages.success(request, 'You registered successfully login now')
            return redirect('accounts:login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form':form})
