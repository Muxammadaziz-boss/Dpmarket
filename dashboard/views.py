from django.shortcuts import render,redirect
from main import models

def index(request):
    return render(request, 'dashboard/index.html')

def create_category(request):
    return render(request, 'dashboard/create_category.html')

def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        logo = request.FILES.get('logo')
        category = models.Category.objects.create(name=name,logo=logo )
    return render(request, 'dashboard/create_product.html')