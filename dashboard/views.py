from django.shortcuts import render,redirect
from main import models
from django.contrib import messages

def index(request):
    return render(request, 'dashboard/index.html')

def create_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        logo = request.FILES.get('logo')
        if name and logo:
            try:
                models.Category.objects.create(name=name, logo=logo)
                messages.success(request, 'Kategoriya muvaffaqiyatli qo\'shildi!')
                return redirect('dashboard_index')
            except Exception as e:
                messages.error(request, f'Xatolik: {str(e)}')
    return render(request, 'dashboard/create_category.html')

def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category_id = request.POST.get('category')
        image = request.FILES.get('image')
        
        if name and description and price and category_id and image:
            try:
                category = models.Category.objects.get(id=category_id)
                models.Product.objects.create(
                    name=name,
                    description=description,
                    price=price,
                    category=category,
                    image=image
                )
                messages.success(request, 'Mahsulot muvaffaqiyatli qo\'shildi!')
                return redirect('dashboard_index')
            except Exception as e:
                messages.error(request, f'Xatolik: {str(e)}')
    
    categories = models.Category.objects.all()
    context = {'categories': categories}
    return render(request, 'dashboard/create_product.html', context)

def create_service(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        duration = request.POST.get('duration')
        image = request.FILES.get('image')
        
        if name and description and price and duration:
            try:
                models.Service.objects.create(
                    name=name,
                    description=description,
                    price=price,
                    duration=duration,
                    image=image if image else None
                )
                messages.success(request, 'Xizmat muvaffaqiyatli qo\'shildi!')
                return redirect('dashboard_index')
            except Exception as e:
                messages.error(request, f'Xizmatni saqlashda xatolik: {str(e)}')
    
    return render(request, 'dashboard/create_service.html')