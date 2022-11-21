from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('', views.mainpage, name='mainpage'),
                  path('buy/<int:id>/', views.buy, name='buy'),
                  path('product/<int:id>/', views.product_site, name='product'),
                  path('login/', views.login_page, name='login'),
                  path('register/', views.register_page, name='register'),
                  path('logout/', views.logout_page, name='logout'),
                  path('active/', views.active, name='active'),
                  path('crate/', views.create, name='create'),
                  path('messages/', views.message_page, name='messages'),
                  path('delete/<int:id>/', views.delete_photo, name='delete'),
                  path('madeoffers/', views.made_offers, name='madeoffers'),
                  path('decline/<int:id>/', views.decline_message, name='decline'),
                  path('accept/<int:id>/', views.accept_message, name='accept'),
                  path('edit/<int:id>/', views.edit, name='edit'),
                  path('counteroffer/<int:id>/', views.counteroffer, name='counteroffer'),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
