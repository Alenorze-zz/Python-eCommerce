from django.shortcuts import render
from django.views.generic import ListView, DetailView

class CartHomeView(DetailView):
    # queryset = Product.objects.all().featured()
    template_name = "products/featured-detail.html"