from django.urls import path, include
from . import views
from .views import CommentsDetail

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('comment/', views.comment, name='comment'),
    path('accounts/profile/', views.profile, name='profile'),
    path('order-online/', views.order_online, name='order-online'),
    path('ajax/', views.add_ajax),
    path('ajax_comment/', views.add_comment),
    path('comments/', CommentsDetail.as_view()),
    path('ajax_comments/', CommentsDetail.as_view()),

]
