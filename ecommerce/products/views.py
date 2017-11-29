from django.shortcuts import render
from django.views.generic import ListView

from .models import Product

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"
