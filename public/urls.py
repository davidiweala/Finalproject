from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('login/', views.userlogin, name="userlogin"),
    path('register/', views.register, name="userregister"),
    path('cart/', views.cart, name="cart"),
    path('shop/', views.shop, name="shop"),
    path('', views.home, name="homepage")
]