from django.shortcuts import render

from .models import Cart


def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    return cart_obj


def cart_home(request):
    cart_id = request.session.get("cart_id", None)
    if cart_id is None:
        cart_obj = cart_create()
        request.session['cart_id'] = cart_obj.id
    else:
        qs = Cart.objects.filter(id=cart_id)
        if qs.count() == 1:
            cart_obj = qs.first()
        else:
            cart_obj = cart_create()
            request.session['cart_id'] = cart_obj.id
    return render(request, "carts/home.html", {})
