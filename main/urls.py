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
    path('add-wishlist/<str:product_code>/', views.add_wishlist, name='add_wishlist'),
    path('delete-wishlist/<str:product_code>/', views.delete_wishlist, name='delete_wishlist'),
    path('wishlist/', views.wishlist, name='wishlist')

]