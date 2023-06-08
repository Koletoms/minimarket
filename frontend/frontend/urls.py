from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name="frontend/index.html")),
    path('about/', TemplateView.as_view(template_name="frontend/delivery.html")),
    path('cart/', TemplateView.as_view(template_name="frontend/cart.html")),
    path('catalog/', TemplateView.as_view(template_name="frontend/catalog.html")),
    path('catalog/<int:pk>', TemplateView.as_view(template_name="frontend/catalog.html")),
    path('order/<int:pk>', TemplateView.as_view(template_name="frontend/oneorder.html")),
    path('order/', TemplateView.as_view(template_name="frontend/order.html")),
    path('delivery/', TemplateView.as_view(template_name="frontend/delivery.html")),
    path('payment/<int:pk>', TemplateView.as_view(template_name="frontend/payment.html")),
    # path('payment-someone/', TemplateView.as_view(template_name="frontend/paymentsomeone.html")),
    path('product/<int:pk>', TemplateView.as_view(template_name="frontend/product.html"), name="product_detail"),
    path('account/', TemplateView.as_view(template_name="frontend/account.html")),
    path('account/profile/', TemplateView.as_view(template_name="frontend/profile.html")),
    # path('progress-payment/', TemplateView.as_view(template_name="frontend/progressPayment.html")),
    path('sale/', TemplateView.as_view(template_name="frontend/sale.html")),
]
