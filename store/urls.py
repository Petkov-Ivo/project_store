from django.urls import path

from store.views import store, cart, checkout, updateItem, create_product, get_shoes, delete_product, product_details, \
    edit_product

urlpatterns = [
    path('', store, name='store'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),

    path('update_item/', updateItem, name='update_item'),
    path('detail/<int:pk>/', product_details, name='product_details'),
    path('create/', create_product, name='create product'),
    path('edit/<int:pk>', edit_product, name='edit_product'),
    path('delete/<int:pk>', delete_product, name='delete_product'),
    path('shoes/', get_shoes, name='get shoes'),
]
