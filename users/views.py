from django.shortcuts import render
from django.views.generic import TemplateView


class AccountView(TemplateView):
    template_name = 'users/acount.html'


class CartView(TemplateView):
    template_name = 'users/cart.html'


class LoginView(TemplateView):
    template_name = 'users/login.html'


class RegisterView(TemplateView):
    template_name = 'users/register.html'


class Reset_PasswordView(TemplateView):
    template_name = 'users/reset-password.html'


class WishListView(TemplateView):
    template_name = 'users/wishlist.html'
