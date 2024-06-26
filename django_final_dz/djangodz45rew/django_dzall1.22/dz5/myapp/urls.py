from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.client_list, name='client_list'),
    path('clients/create/', views.create_client, name='create_client'),
    path('clients/update/<int:client_id>/', views.update_client, name='update_client'),
    path('clients/delete/<int:client_id>/', views.delete_client, name='delete_client'),
    path('clients/<int:client_id>/products/', views.client_product_list, name='client_product_list'),
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.create_product, name='create_product'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/create/', views.create_order, name='create_order'),
]
