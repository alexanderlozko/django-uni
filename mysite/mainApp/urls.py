from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('comment/', views.comment, name='comment'),
    path('order-online/', views.order_online, name='order-online'),
    path('ajax/', views.add_ajax),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),

]
