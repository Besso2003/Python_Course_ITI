from django.urls import path
from products.views import index, show, create, edit, delete

app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('show/<int:id>', show, name='show'),
    path('create', create, name='create'),
    path('edit/<int:id>', edit, name='edit'),
    path('delete/<int:id>', delete, name='delete'),
]
