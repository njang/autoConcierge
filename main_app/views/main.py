from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from main_app.models import CarOwner
from main_app.forms import CarOwnerSignUpForm

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

def profile_car_owner(request, user_id):
    user = CarOwner.objects.get(user=user_id)
    return render(request, 'profile/car_owner.html', {'user': user})

def error_404(request):
    data = {}
    return render(request,'404.html', data)
 
def error_500(request):
    data = {}
    return render(request,'500.html', data)