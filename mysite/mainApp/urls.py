from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('comment/', views.comment, name='comment'),
    path('accounts/profile/', views.profile, name='profile'),
    path('order-online/', views.order_online, name='order-online'),

]
