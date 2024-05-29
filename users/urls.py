from django.urls import path

from users.views import *

app_name = 'users'

urlpatterns = [
    path('account/', AccountView.as_view(), name='account'),
    path('login/', LoginView.as_view(), name='login'),
    path('wishlist/', WishListView.as_view(), name='wishlist'),
    path('register/', RegisterView.as_view(), name='register'),
    path('reset-password/', Reset_PasswordView.as_view(), name='reset-password'),
    path('cart/', CartView.as_view(), name='cart'),
]