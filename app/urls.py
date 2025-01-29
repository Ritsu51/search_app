from django.urls import path, include
from django.contrib import admin

from . import views

app_name = "app"

urlpatterns = [
    path('', views.product_list),
    path('search/', views.search_view, name='search_view'),
    path('product/new/', views.product_create, name='product_create'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:pk>/edit/', views.product_update, name='product_update'),
    path('product/<int:pk>/delete', views.product_delete, name='product_delete'),
    path('product/', views.product_list, name='product_list'),
    path('follow/<int:pk>/', views.Favorite_page, name='follow_place'),
    path('product/description/<int:pk>/', views.Product_description, name='product_description'),
]