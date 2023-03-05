from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse

# Create your views here.
data = {
    'telefon':'telefon kategorisindeki urunler',
    'bilgisayar':'bilgisayar kategorisindeki urunler',
    'elektronik':'elektronik kategorisindeki urunler',
}
def index(request):
    return HttpResponse('Hello')

def getProductsByCategory(request, category):
    try:
        category_text=data[category]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound('yanlis kategori')

def getProductsByCategoryId(request, categoryId):
    category_list = list(data.keys())
    if categoryId > len(category_list):
        return HttpResponseNotFound('yanlis kategori secimi')
    
    category_name = category_list[categoryId-1]
    redirected_path = reverse('getProductsByCategory', args=[category_name])
    return redirect(redirected_path)