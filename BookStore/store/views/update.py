from django.shortcuts import render, redirect
from django.views import View

from store.models import Customer
from store.models.product import Product
from store.models.orders import Order
from store.middlewares.auth import auth_middleware


from store.models.category import Category


class UpdateOrder(View):


        def get(self, request):
                customer = request.session.get('customer')
                orders = Order.get_orders_by_customer(customer)
                print(orders)
                return render(request, 'update.html', {'orders' : orders})
