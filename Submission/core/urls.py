from .views import *
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
]