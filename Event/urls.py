from django.urls import path
from . import views


urlpatterns = [
    path('', views.Event, name='event')
]