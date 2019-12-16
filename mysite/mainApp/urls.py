from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('comment/', views.comment, name='comment'),
    path('back-call/', views.backcall, name='backcall'),
    path('order-online/', views.order_online, name='order-online'),
    path('thanks/', views.thanks, name='thanks'),
    path('leave_comment/', views.leave_comment, name='leave_comment'),
    path('thanks_for_the_comment/', views.thanks_for_the_comment, name='thanks_for_the_comment'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('ajax/', views.add_ajax),

    path('order/', views.order, name='order'),

]
