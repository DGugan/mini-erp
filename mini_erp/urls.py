from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from core.views import (
    dashboard_view,
    products_view,
    add_product_view,
    edit_product_view,
    delete_product_view
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('dashboard/', dashboard_view, name='dashboard'),

    path('products/', products_view, name='products'),
    path('products/add/', add_product_view, name='add_product'),
    path('products/edit/<int:product_id>/', edit_product_view, name='edit_product'),
    path('products/delete/<int:product_id>/', delete_product_view, name='delete_product'),
]
