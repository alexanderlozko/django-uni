from django.urls import path
from .views import BackCallView

urlpatterns = [
    path('backcall/', BackCallView.as_view()),

]
