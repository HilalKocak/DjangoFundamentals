from django.urls import path
from movieapp.views import index, getProductsByCategory, getProductsByCategoryId

urlpatterns = [
    path('', index, name='index'),
    path('<int:categoryId>', getProductsByCategoryId, name='getProductsByCategoryId'),

    path('<str:category>', getProductsByCategory, name='getProductsByCategory'),
]