from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

products = [
    {'id': 1, 'name': 'laptop', 'price': 25000, 'stock': 5, 'image': 'laptop.jpg'},
    {'id': 2, 'name': 'mobile', 'price': 15000, 'stock': 10, 'image': 'mobile.jpg'},
    {'id': 3, 'name': 'headphones', 'price': 5000, 'stock': 15, 'image': 'headphone.jpg'},
]

def products_index(request):
    # return HttpResponse(products)
    return render(request, 'products/index.html', context={'products': products})


def product_details(request, product_id):
    
    filter_product = list(filter(lambda p: p['id'] == product_id, products))
    if filter_product:
        product = filter_product[0]
        # return HttpResponse(product)
        return render(request, 'products/detail.html', context={'product': product})
    else:
        return HttpResponse("==== Product not found ====")