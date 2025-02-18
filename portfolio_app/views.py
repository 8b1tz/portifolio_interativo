from django.conf import settings
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RegisterForm
from .models import Interesse, Projeto, UserProfile


def home(request):
    return render(request, 'portfolio_app/home.html')

def sobre(request):
    return render(request, 'portfolio_app/sobre.html')

def listar_projetos(request):
    return render(request, 'portfolio_app/projetos.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']

            if password != password2:
                messages.error(request, 'As senhas não coincidem.')
                return redirect('register')

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Nome de usuário já está em uso.')
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'E-mail já está em uso.')
                return redirect('register')

            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            profile = UserProfile.objects.create(user=user, email_verified=True)
            profile.save()

            messages.success(request, 'Cadastro realizado com sucesso! Faça login.')
            return redirect('login')
        else:
            messages.error(request, 'Erro no formulário (verifique a soma ou os campos).')
    else:
        form = RegisterForm()
    return render(request, 'portfolio_app/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            profile, created = UserProfile.objects.get_or_create(user=user)
            if created:
                profile.email_verified = True
                profile.save()

            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Credenciais inválidas.')
    return render(request, 'portfolio_app/login.html')

def user_logout(request):
    logout(request)
    messages.info(request, 'Você saiu da conta.')
    return redirect('home')

def demonstrar_interesse(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'Faça login para demonstrar interesse.')
            return redirect('sobre')
        if request.user.is_superuser:
            messages.error(request, 'Admin não pode demonstrar interesse.')
            return redirect('sobre')

        ja_existe = Interesse.objects.filter(user=request.user).exists()
        if ja_existe:
            messages.error(request, 'Você já registrou interesse.')
        else:
            mensagem = request.POST.get('mensagem', '')
            Interesse.objects.create(user=request.user, mensagem=mensagem)
            messages.success(request, 'Interesse registrado com sucesso!')
        return redirect('sobre')
    return redirect('sobre')

@staff_member_required
def listar_interesses(request):
    interests = Interesse.objects.all().order_by('-data')
    novos = Interesse.objects.filter(respondido=False).count()
    return render(request, 'portfolio_app/painel_interesses.html', {
        'interesses': interests,
        'novos': novos,
    })

@staff_member_required
def responder_interesse(request, interest_id):
    interest = get_object_or_404(Interesse, pk=interest_id)
    if request.method == 'POST':
        resposta = request.POST.get('resposta')
        to_email = interest.user.email
        if to_email:
            subject = "Resposta ao seu interesse"
            message = f"Olá, {interest.user.username}\n\n{resposta}"
            from_email = settings.EMAIL_HOST_USER or 'no-reply@example.com'
            send_mail(subject, message, from_email, [to_email], fail_silently=False)
            interest.respondido = True
            interest.save()
            messages.success(request, 'Resposta enviada com sucesso!')
        else:
            messages.error(request, 'Este usuário não possui e-mail cadastrado.')
        return redirect('listar_interesses')
    
    interests = Interesse.objects.all().order_by('-data')
    return render(request, 'portfolio_app/painel_interesses.html', {
        'interesses': interests,
        'interesse_foco': interest,
    })
