from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from main_app.models import User, CarOwner, ShopOwner, ServiceDriver, Car
from main_app.forms import AddCarForm

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

def add_car_form(request):
    form = AddCarForm()
    return render(request, 'add_car.html', {'form': form})

def add_car(request):
    form = AddCarForm(request.POST)
    if form.is_valid():
        car = form.save(commit = False)
        if (len(car.car_make) == 3 and car.car_make != 'kia'):
            car.car_make = car.car_make.upper()
        else:    
            car.car_make = car.car_make.title()
        car.owner = request.user
        car.save()
    path = '/' + str(request.user.id) + '/profile/'
    return HttpResponseRedirect(path)

def show_car(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'show_car.html', {'car': car})

def edit_car(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'show_car.html', {'car': car})

def remove_car(request, car_id):
    Car.objects.get(id=car_id).delete()
    path = '/' + str(request.user.id) + '/profile/'
    return HttpResponseRedirect(path)

def error_404(request):
    data = {}
    return render(request,'404.html', data)
 
def error_500(request):
    data = {}
    return render(request,'500.html', data)