from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, ListView, UpdateView
from django.http import HttpResponseRedirect
from main_app.forms import ShopOwnerSignUpForm, EditShopForm
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
        path = '/' + str(user.id) + '/profile/'
        return redirect(path)

def edit_shop(request, user_id):
    shop = ShopOwner.objects.get(user=user_id)
    form = EditShopForm({'shop_name': shop.shop_name, 'address_street': shop.address_street, 'phone_number': shop.phone_number})
    return render(request, 'edit_shop.html', {'shop': shop, 'form': form})

def update_shop(request, shop_id):
    form = EditShopForm(request.POST)
    if form.is_valid():
        shop = ShopOwner.objects.get(id=shop_id)
        shop.shop_name = form.cleaned_data['shop_name']
        shop.address_street = form.cleaned_data['address_street']
        shop.phone_number = form.cleaned_data['phone_number']
        shop.save()
    path = '/' + str(request.user.id) + '/profile/'
    return HttpResponseRedirect(path)