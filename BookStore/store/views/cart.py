from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Product
from store.middlewares.auth import auth_middleware

class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        return render(request, 'cart.html', {'products' : products})
