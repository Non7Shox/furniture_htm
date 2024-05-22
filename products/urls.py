from django.urls import path

from products.views import ProductsListView, ProductsDetailView

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='list'),
    path('detail/<int:pk>/', ProductsDetailView.as_view(), name='detail'),
]
