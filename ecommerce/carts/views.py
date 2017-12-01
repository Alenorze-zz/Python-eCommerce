from django.shortcuts import render


def cart_home(request):
    cart_id = request.session.get("cart_id", None)
    if cart_id is None:
        request.session['cart_id'] = 12
    return render(request, "carts/home.html", {})