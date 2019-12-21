from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('comment/', views.comment, name='comment'),
    path('thanks/', views.thanks, name='thanks'),
    path('thanks_for_the_comment/', views.thanks_for_the_comment, name='thanks_for_the_comment'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('ajax/', views.add_ajax),
]
