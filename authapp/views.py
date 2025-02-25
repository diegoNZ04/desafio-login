import re
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from desafiologin import settings
from .models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        
        if not email or not password:
            messages.error(request, 'Email e senha são obrigatórios')
            return redirect('login')
        
        user = User.objects.filter(email=email).first()
        if not user:
            messages.error(request, 'Email inexistente.')
            return redirect('login')
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('menu')
        else:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Senha inválida.')
            else:
                messages.error(request, 'Email inválido.')
    
    return render(request, 'authapp/login.html')

def register_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        confirmpassword = request.POST.get('confirmpassword', '').strip()
        
        if not name or not re.match(r'^[A-Za-zÀ-ÿ\s]+$', name):
            messages.error(request, 'O nome deve conter apenas letras e não pode estar vazio.')
            return redirect('register')
        
        if not email or '@' not in email:
            messages.error(request, 'Email inválido')
            return redirect('register') 
        
        if len(password) < 8 or not re.search(r'[A-Z]', password) or not re.search(r'[0-9]', password) or not re.search(r'[\W_]', password):
            messages.error(request, 'A senha deve ter pelo menos 8 caracteres, um número, uma letra maiúscula e um caractere especial.')
            return redirect('register')   
            
        if password != confirmpassword:
            messages.error(request, 'Senhas não conferem')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado')
            return redirect('register')
        
        user = User.objects.create_user(username=email, email=email, password=password, name=name)
        user.set_password(password)
        user.save()
        
        subject = "Bem vindo à Fidelity!"
        message = f"Olá, {name}!\n\nSeu cadastro ao Desafio Técnico da Fidelity foi realizado com sucesso.\n\nSeja bem-vindo!"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        
        
        messages.success(request, "Cadastro realizado com sucesso! Faça login.")
        return redirect('login')
    
    return render(request, 'authapp/register.html')

@login_required
def menu_view(request):
    return render(request, 'authapp/menu.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')