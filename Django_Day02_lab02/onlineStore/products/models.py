from django.db import models
from django.urls import reverse
from django.shortcuts import get_object_or_404

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    stock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.CharField(max_length=255, null=True, blank=True)  # can be a URL or path
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.name}({self.id})"

    @property
    def show_url(self):
        url = reverse('products:show', args=[self.id])
        return url

    @property    
    def delete_url(self):
        delete_url = reverse('products:delete', args=[self.id])
        return delete_url

    @property
    def edit_url(self):
        edit_url = reverse('products:edit', args=[self.id])
        return edit_url

    @classmethod
    def get_all(cls):
        return cls.objects.all().order_by('id')

    @classmethod
    def delete_object_by_id(cls, id):
        product = get_object_or_404(cls, id=id)
        product.delete()
        return True

