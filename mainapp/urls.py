from django.urls import path

from .views import index, products, product, about, contacts

urlpatterns = [
    path('', index),
    path('products/', products),
    path('product/<int:product_id>/', product),
    path('about/', about),
    path('contacts/', contacts)
]
