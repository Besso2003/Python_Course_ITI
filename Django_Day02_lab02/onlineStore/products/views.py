from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from products.models import Product

# Create your views here.

# List all products
def index(request):
    products = Product.get_all()
    print(products)
    return render(request, 'products/index.html', context={'products': products})

# Show a single product
def show(request, id):
    product = get_object_or_404(Product, id=id)
    print(product)
    return render(request, 'products/show.html', context={'product': product})

# Delete a product
def delete(request, id):
    deleted = Product.delete_object_by_id(id)
    print(deleted)
    return redirect('products:index')

# Create a new product
def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        stock = request.POST['stock']
        price = request.POST['price']
        image = request.POST.get('image', '')  # optional
        description = request.POST.get('description', '')

        product = Product(
            name=name,
            stock=int(stock),
            price=float(price),
            image=image,
            description=description
        )
        product.save()
        return redirect(product.show_url)

    return render(request, 'products/create.html')

# Edit a product
def edit(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.stock = int(request.POST['stock'])
        product.price = float(request.POST['price'])
        product.image = request.POST.get('image', product.image)
        product.description = request.POST.get('description', product.description)
        product.save()
        return redirect(product.show_url)

    return render(request, 'products/edit.html', {'product': product})
