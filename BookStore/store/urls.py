from django.urls import path
from django.contrib import admin
from .views.home import Index
from .views.signup import Signup
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.cancel import CancelOrderView
from .views.update import UpdateOrder
from .middlewares.auth import auth_middleware
from store.views import payment
from store.views import payment2





urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('cancel', CancelOrderView.as_view(), name='cancel'),
    path('update', auth_middleware(UpdateOrder.as_view()), name='update'),
    path('payment', payment.homepage, name='index'),
    path('payment2', payment2.paymenthandler, name='index2'),
    
] 


