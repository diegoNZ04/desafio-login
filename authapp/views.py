from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('menu')
        else:
            messages.error(request, 'Email ou senha inválidos')
    
    return render(request, 'authapp/login.html')

def register_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST["confirmpassword"]
        
        if password != confirmpassword:
            messages.error(request, 'Senhas não conferem')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado')
            return redirect('register')
        
        user = User.objects.create_user(email=email, password=password, name=name)
        user.save()
        messages.success(request, "Cadastro realizado com sucesso! Faça login.")
        return redirect('login')
    
    return render(request, 'authapp/register.html')

@login_required
def menu_view(request):
    return render(request, 'authapp/menu.html')

def logout_view(request):
    logout(request)
    return redirect('login')