from django.urls import path
from . import views
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
                  path('messages_buy/', views.message_page_buy, name='messages_buy'),
                  path('messages_sell/', views.message_page_sell, name='messages_sell'),
                  path('delete/<int:id>/', views.delete_photo, name='delete'),
                  path('madeoffers/', views.made_offers, name='madeoffers'),
                  path('madeoffers_buy/', views.made_offers_buy, name='madeoffers_buy'),
                  path('madeoffers_sell/', views.made_offers_sell, name='madeoffers_sell'),
                  path('decline/<int:id>/', views.decline_message, name='decline'),
                  path('accept/<int:id>/', views.accept_message, name='accept'),
                  path('edit/<int:id>/', views.edit, name='edit'),
                  path('counteroffer/<int:id>/', views.counteroffer, name='counteroffer'),
                  path('delete_message/<int:id>/', views.delete_message, name='delete_message'),
                  path('archive_offers/', views.archive_offers, name='archive_offers'),
                  path('archivize/<int:id>/', views.archivize_message, name='archivize'),
                  path('confirm_payment/<int:id>/', views.confirm_payment, name='confirm_payment')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
