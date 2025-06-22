from django.urls import path
from . import views

urlpatterns = [
    path('', views.invitacion, name='invitacion'),
]
