"""minimarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from rest_framework.routers import SimpleRouter

from basket_app.api import ProductInBasketViewSet
from minimarket import settings
from payment_app.api import PaymentViewSet
from shop_app.api import CategoryViewSet, ProductViewSet, ReviewViewSet, ProductLimitedViewSet, ProductPopularViewSet, \
    CatalogViewSet, TagViewSet, BannerViewSet
from user_app.api import ProfileDetailAPIView, AccountDetailAPIView
from order_app.api import OrderViewSet, OrderActiveViewSet, DeliveryViewSet

# router = routers.SimpleRouter()
# router.register('api/categories/', CategoryViewSet)
#

urlpatterns = [
    path("", include("frontend.urls")),

    path('admin/', admin.site.urls),
    path('user/', include('user_app.urls')),

    path('api/profile/', ProfileDetailAPIView.as_view()),
    path('api/account/', AccountDetailAPIView.as_view()),
    path('api/categories/', CategoryViewSet.as_view({'get': 'list'})),
    path('api/catalog/', CatalogViewSet.as_view({'get': 'list'})),
    path('api/tags/', TagViewSet.as_view({'get': 'list'})),
    path('api/banners/', BannerViewSet.as_view({'get': 'list'})),
    path('api/delivery/', DeliveryViewSet.as_view({'get': 'list'})),
    path('api/orders/', OrderViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/orders/<int:pk>', OrderViewSet.as_view({'get': 'retrieve', 'post': 'update'})),
    path('api/orders/active/', OrderActiveViewSet.as_view({'get': 'retrieve'})),
    path('api/payment/<int:pk>', PaymentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/basket/', ProductInBasketViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/basket/<int:pk>', ProductInBasketViewSet.as_view({'delete': 'destroy', 'put': 'update'})),
    path('api/products/limited/', ProductPopularViewSet.as_view({'get': 'list'})),
    path('api/products/popular/', ProductLimitedViewSet.as_view({'get': 'list'})),
    path('api/products/<int:pk>', ProductViewSet.as_view({'get': 'retrieve'})),
    path('api/products/<int:pk>/review/', ReviewViewSet.as_view({'post': 'create'}))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #+ router.urls
