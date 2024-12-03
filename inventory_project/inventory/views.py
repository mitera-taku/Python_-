from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        price = request.POST['price']
        description = request.POST.get('description', '')
        Product.objects.create(name=name, quantity=quantity, price=price, description=description)
        return redirect('product_list')
    return render(request, 'inventory/add_product.html')

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.quantity = request.POST['quantity']
        product.price = request.POST['price']
        product.description = request.POST.get('description', '')
        product.save()
        return redirect('product_list')
    return render(request, 'inventory/edit_product.html', {'product': product})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')
