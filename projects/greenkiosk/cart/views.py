from django.urls import path
from . import views


urlpatterns = [
    path('cart/add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
]
10:26
from django.shortcuts import render, redirect
from .models import Cart
from inventory.models import Productdef add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)
    cart.products.add(product)
    return redirect('view_cart')


def view_cart(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user).prefetch_related('products')    
    total_price = sum(product.price * product.quantity for cart in cart_items for product in cart.products.all())    
    print("Cart Items:", cart_items)
    print("Total Price:", total_price)    
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart/view_cart.html', context)

