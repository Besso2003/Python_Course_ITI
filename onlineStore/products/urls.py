from django.urls import path
from products.views import products_index, product_details

app_name = 'products'

urlpatterns = [
    path('', products_index, name='index'),
    path('index/<int:product_id>/', product_details, name='details'),
]
