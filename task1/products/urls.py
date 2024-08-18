from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('categories/<str:categoryname>/products/', ProductListView.as_view(), name='product-list'),
    path('categories/<str:categoryname>/products/<str:productid>/', ProductDetailView.as_view(), name='product-detail'),
]
