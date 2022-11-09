from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('buy/', views.cart, name='buy'),
    path('checkout/', views.checkout, name='checkout'),
    path('product/', views.product, name='product'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register')
]
