from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return HttpResponse(form.errors)
    else:
        form = UserForm()
    return render(request, 'users/register.html', {'form': form})
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'users/login.html', {'error': 'Невірний email або пароль'})
    return render(request,'users/login.html')

def user_logout(request):
    logout(request)
    return redirect('/')