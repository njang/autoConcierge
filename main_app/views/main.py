from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from main_app.models import User, CarOwner, ShopOwner, ServiceDriver, Car
from main_app.forms import AddCarForm, ShopOwnerSignUpForm, EditShopForm

# Create your views here.
def index(request):
	return render(request, 'index.html')

class SignUpView(TemplateView):
    template_name = 'signup.html'

def signup(request):
    return render(request, 'signup.html')

def signup_car_owner(request):
	return render(request, 'registration/car_owner.html')

def signup_shop_owner(request):
    return render(request, 'registration/shop_owner.html')

def signup_service_driver(request):
    return render(request, 'registration/service_driver.html')

def profile(request, user_id):
    user = User.objects.get(id=user_id)
    cars = Car.objects.filter(owner=request.user)
    if user.is_car_owner:
        user_info = CarOwner.objects.get(user=user_id)
    elif user.is_shop_owner:
        user_info = ShopOwner.objects.get(user=user_id)
    else:
        user_info = ServiceDriver.objects.get(user=user_id)
    return render(request, 'profile/profile.html', {'user': user, 'user_info': user_info, 'cars': cars})

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

def error_404(request):
    data = {}
    return render(request,'404.html', data)
 
def error_500(request):
    data = {}
    return render(request,'500.html', data)