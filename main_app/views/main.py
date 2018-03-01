from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from main_app.models import User, CarOwner, ShopOwner, ServiceDriver
# from main_app.forms import CarOwnerSignUpForm

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
    if user.is_car_owner:
        user = ShopOwner.objects.get(user=user_id)
    elif user.is_shop_owner:
        user = ShopOwner.objects.get(user=user_id)
    else:
        user = ServiceDriver.objects.get(user=user_id)
    return render(request, 'profile/profile.html', {'user': user})

def error_404(request):
    data = {}
    return render(request,'404.html', data)
 
def error_500(request):
    data = {}
    return render(request,'500.html', data)