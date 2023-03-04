from django.urls import path
from movieapp.views import index

urlpatterns = [
    path('', index, name='index')
]