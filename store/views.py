from django.shortcuts import render
from store.models import Product
from django.shortcuts import get_object_or_404
from store.models import Cart , Order
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.

def main(request):
    return render(request , "store/main.html")
def index(request):

    #Qui permet de recuperer les produits
    products = Product.objects.all()
    return render(request, 'store/index.html' ,context={"products":products})

def product_detail(request , slug):

    product = get_object_or_404(Product ,slug = slug) 
    return render(request , "store/detail.html" , context={"product":product})

def add_to_cart(request , slug):
    user = request.user
    product  = get_object_or_404(Product , slug = slug)
    cart , _ = Cart.objects.get_or_create(user=user)
    order , created = Order.objects.get_or_create(user=user , ordered = False , product = product)

    if created : 
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()
    return redirect(reverse("product" , kwargs={"slug":slug}))
def cart (request):

    cart = get_object_or_404(Cart , user = request.user)
    return render(request , "store/cart.html" , context={"orders":cart.orders.all()})

def delete_cart(request):
    cart = request.user.cart

    if (cart):
        cart.orders.all().delete()
        cart.delete()

    return redirect("index")