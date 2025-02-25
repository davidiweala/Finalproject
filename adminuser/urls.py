from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('x2c3v4b5n6m7/', views.adminlogin, name="adminlogin"),
    path('x2c3v4b5n6/', views.register, name="adminregister"),
    path('admindash/', views.dashboard, name="admindash")
]