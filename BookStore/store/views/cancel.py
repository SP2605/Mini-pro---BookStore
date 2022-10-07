from django.shortcuts import render, redirect
from django.views import View

from store.models import Customer
from store.models.product import Product
from store.models.orders import Order
from store.middlewares.auth import auth_middleware

class CancelOrderView(View):


    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)      
        return render(request, 'cancel.html', {'orders' : orders})

    def post(self, request, *args, **kwargs):
        if request.method=="POST":
            order_ids = request.POST.getlist('id[]')
            for id in order_ids:
                order = Order.objects.get(pk=id)
                order.delete()
            return redirect('update')




  


