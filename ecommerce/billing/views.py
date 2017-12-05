import stripe
from django.shortcuts import render


stripe.api_key = "sk_test_hlp4fgMTihQnCQkWp5bj2Suw"

STRIPE_PUB_KEY = 'pk_test_D8FSbsJiS8Lfk8sVGdyxOJf1'


def payment_method_view(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, 'billing/payment-method.html', {"publish_key": STRIPE_PUB_KEY})