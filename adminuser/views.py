from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm


def logoutpage(request):
    logout(request)
    return redirect('adminlogin')


def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('admindash')
        else:
            messages.info(request, 'Invalid Details')
    return render(request, 'adminlogin.html')



def register(request):
    form = RegistrationForm()
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created successfully' + username)
            return redirect('adminlogin')

    context = {'form': form}

    return render(request, 'adminregister.html', context)


def dashboard(request):
    return render(request, 'admindash.html')


