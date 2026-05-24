from django.urls import path
from . import  views
urlpatterns = [
    path('',views.index,name='index'),
    path('product-detail/<str:code>/', views.product_detail, name='product_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('category-filter/<int:category_id>/', views.category_filter, name='category_filter'),
    path('products/category/<int:category_id>/', views.category_filter, name='index_by_category'),
    path('add-to-cart/<str:product_code>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<str:product_code>/', views.remove_from_cart, name='remove_from_cart'),
    path('update-cart-quantity/<str:product_code>/', views.update_cart_quantity, name='update_cart_quantity'),
    path('add-wishlist/<str:product_code>/', views.add_wishlist, name='add_wishlist'),
    path('delete-wishlist/<str:product_code>/', views.delete_wishlist, name='delete_wishlist'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('cart/', views.cart, name='cart'),

]
