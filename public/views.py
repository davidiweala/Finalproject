from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from django.contrib import messages


def logoutpage(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'generalhome.html')

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('cart')
        else:
            messages.info(request, 'Invalid Details')
    return render(request, 'generallogin.html')


def register(request):
    form = RegistrationForm()
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created successfully' + username)
            return redirect('userlogin')

    context = {'form': form}

    return render(request, 'generalregister.html', context)


def cart(request):
    return render(request, 'cart.html')


def shop(request):
    return render(request, 'shop.html')