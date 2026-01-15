from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Product


@login_required
def dashboard_view(request):
    product_count = Product.objects.count()
    user_count = User.objects.count()

    return render(request, 'dashboard.html', {
        'product_count': product_count,
        'user_count': user_count
    })


@login_required
def products_view(request):
    products = Product.objects.all()
    return render(request, 'products.html', {
        'products': products
    })


@login_required
def add_product_view(request):
    if request.method == 'POST':
        Product.objects.create(
            name=request.POST.get('name'),
            price=request.POST.get('price'),
            quantity=request.POST.get('quantity')
        )
        return redirect('products')

    return render(request, 'add_product.html')


@login_required
def edit_product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.quantity = request.POST.get('quantity')
        product.save()
        return redirect('products')

    return render(request, 'edit_product.html', {
        'product': product
    })


@login_required
def delete_product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('products')
