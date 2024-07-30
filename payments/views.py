import stripe
from django.http import JsonResponse
from django.views import View
from .services import create_stripe_product, create_stripe_price, create_stripe_checkout_session


class CreatePaymentView(View):
    http_method_names = ['post']  # Allow only POST requests

    @staticmethod
    def post(request):
        product_name = request.POST.get('product_name')
        product_price = int(request.POST.get('product_price')) * 100  # Convert to cents

        product = create_stripe_product(product_name)
        price = create_stripe_price(product['id'], product_price)
        session = create_stripe_checkout_session(price['id'], 'https://example.com/success',
                                                 'https://example.com/cancel')

        return JsonResponse({'checkout_url': session.url})


class RetrievePaymentStatusView(View):
    @staticmethod
    def get(request, session_id):
        session = stripe.checkout.Session.retrieve(session_id)
        return JsonResponse({'payment_status': session.payment_status})
