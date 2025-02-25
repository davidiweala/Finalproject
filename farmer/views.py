from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from django.contrib import messages
from .models import Sensor
import requests


def logoutpage(request):
    logout(request)
    return redirect('farmerlogin')

def home(request):
    return render(request, 'farmerhome.html')


def farmerlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('farmerdash')

    return render(request, 'farmerlogin.html')


def register(request):
    form = RegistrationForm()
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created successfully' + username)
            return redirect('farmerlogin')

    context = {'form': form}

    return render(request, 'farmerregister.html', context)


def dashboard(request):
    all_sensors = {}
    url = 'https://api.weatherbit.io/v2.0/history/agweather?lat=38.0&lon=-78.0&start_date=2021-08-11&end_date=2021-08-12&key=b30992333c8e4602b9b3d8a0dcff7bae'
    response = requests.get(url)
    data = response.json()
    print(data)
    sensor = data['data']

    for i in sensor:
        sensor_data = Sensor(
            humidity=i['specific_humidity'],
            temperature=i['skin_temp_avg'],
            soil_density=i['bulk_soil_density'],
            precipitation=i['precip'],
            solar_radiation=i['dlwrf_avg'],
            surface_pressure=i['pres_avg']
            )
        sensor_data.save()
        all_sensors = Sensor.objects.all()

    return render(request, 'farmerdash.html', {"all_sensors": all_sensors})