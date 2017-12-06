import stripe
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.utils.http import is_safe_url

stripe.api_key = 'sk_test_hlp4fgMTihQnCQkWp5bj2Suw'

STRIPE_PUB_KEY = 'pk_test_D8FSbsJiS8Lfk8sVGdyxOJf1'


def payment_method_view(request):
    next_url = None
    next_ = request.GET.get('next')
    if is_safe_url(next_, request.get_host()):
        next_url = next_
    return render(request, 'billing/payment-method.html', {"publish_key": STRIPE_PUB_KEY})


def payment_method_createview(request):
    if request.method == "POST" and request.is_ajax():
        return JsonResponse({"message": "Done"})
    return HttpResponse("error", status_code=401)
