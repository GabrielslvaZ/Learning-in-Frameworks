from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Pessoa
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

def home(request):
    return HttpResponse("<h1>Apenas Igniore está tela!</h1>")

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(f"Email digitado: {email}")
        print(f"Senha digitada: {password}")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {"error": "Credenciais inválidas"})
    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = request.POST.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            if user is not None:
                login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

def custom_404(request, exception):
    return render(request, 'errors/404.html', status=404)

def custom_500(request):
    return render(request, 'errors/500.html', status=500)

def custom_403(request, exception):
    return render(request, 'errors/403.html', status=403)

@login_required
def profile(request):
    # Se houver um parâmetro GET ?user_id=, permitir que staff/administradores vejam outros perfis
    user_id = request.GET.get('user_id')
    target_user = None
    if user_id and request.user.is_staff:
        target_user = get_object_or_404(User, pk=user_id)
    else:
        target_user = request.user

    try:
        pessoa = Pessoa.objects.select_related('usuario', 'endereco').get(usuario=target_user)
    except Pessoa.DoesNotExist:
        pessoa = None

    # Indica se o usuário atual está apenas vendo seu próprio perfil
    is_own_profile = (target_user == request.user)
    return render(request, 'perfil.html', {'pessoa': pessoa, 'is_own_profile': is_own_profile, 'target_user': target_user})

def pessoas_list(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoas_list.html', {'pessoas': pessoas})

def pessoas_index(request):
    pessoas = Pessoa.objects.select_related('usuario', 'endereco').all()
    return render(request, 'index.html', {'pessoas': pessoas})

