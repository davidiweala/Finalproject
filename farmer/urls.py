from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('farmerlogin/', views.farmerlogin, name="farmerlogin"),
    path('farmerregister/', views.register, name="farmerregister"),
    path('farmerdash/', views.dashboard, name="farmerdash"),
    path('logout/', views.logoutpage, name="logout"),
    path('farmerhome/', views.home, name="farmerhome")
]