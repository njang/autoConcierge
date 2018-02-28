from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, ListView, UpdateView
from main_app.forms import ShopOwnerSignUpForm
from main_app.models import User, ShopOwner
from django.contrib.auth import login

class SignUpView(CreateView):
    model = User
    form_class = ShopOwnerSignUpForm
    template_name = 'registration/shop_owner.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        path = '/' + str(user.id) + '/shop-owner-profile/'
        return redirect(path)