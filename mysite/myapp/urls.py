from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('buy/<int:id>/', views.buy, name='buy'),
    path('product/<int:id>/', views.product_site, name='product'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('active/', views.active, name='active'),
    path('crate/', views.create, name='create'),
    path('messages/', views.messages, name='messages')
]
