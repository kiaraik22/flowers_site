from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import  messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm


from .models import Profile

# Create your views here.


def register_user(request):

    page = 'register'

    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save() # сохраняем все данные из формы
            user.username = user.username.lower()
            user.save()

            messages.success(request, f'Учетная запись пользователя создана {user.username}')
            login(request, user)
            return redirect('account')
        else:
            messages.error(request, "Не удалось зарегестрироваться.")


    context = {
        'page':page,
        'form':form
    }


    return render(request, 'users/login.html',context)

def login_user(request):

    if request.user.is_authenticated:
        return redirect('menu.index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request,"Имя пользователя не найдено")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('account')
        else:
            messages.error(request,"Неверное имя пользователя или пароль")



    return  render(request, 'users/login.html')


def logout_user(request):
    logout(request)
    messages.error(request,"Пользователь вышел")

    return redirect('login')



@login_required(login_url='login')
def my_account(request):
    profile = request.user.profile

    context = {
        'profile':profile,
    }
    return render(request, "users/my-account.html", context)

def user_profile(request, pk):
    profile = get_object_or_404(Profile, id=pk)
    return render(request, 'users/my-account.html', {'profile': profile})