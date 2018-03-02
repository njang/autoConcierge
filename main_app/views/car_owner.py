from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, ListView, UpdateView
from django.http import HttpResponseRedirect
from main_app.forms import CarOwnerSignUpForm
from main_app.models import User, CarOwner, Car, ShopOwner, Service
from django.contrib.auth import login

class SignUpView(CreateView):
    model = User
    form_class = CarOwnerSignUpForm
    template_name = 'registration/car_owner.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        path = '/' + str(user.id) + '/profile/'
        return redirect(path)

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
    form = AddCarForm({'car_year': car.car_year, 'car_make': car.car_make, 'car_model': car.car_model, 'car_model_trim': car.car_model_trim, 'car_color': car.car_color, 'car_license': car.car_license, 'loc_parking': car.loc_parking})
    return render(request, 'edit_car.html', {'car': car, 'form': form})

def update_car(request, car_id):
    form = AddCarForm(request.POST)
    if form.is_valid():
        car = form.save(commit = False)
        if (len(car.car_make) == 3 and car.car_make != 'kia'):
            car.car_make = car.car_make.upper()
        else:    
            car.car_make = car.car_make.title()
        car.id = car_id
        car.owner = request.user
        car.save()
    path = '/' + str(request.user.id) + '/profile/'
    return HttpResponseRedirect(path)

def remove_car(request, car_id):
    Car.objects.get(id=car_id).delete()
    path = '/' + str(request.user.id) + '/profile/'
    return HttpResponseRedirect(path)

def service_car(request, car_id):
    car = Car.objects.get(id=car_id)
    shops = ShopOwner.objects.all()
    return render(request, 'request_service.html', {'car': car, 'shops': shops})

def post_request(request, car_id):
    form = AddCarForm(request.POST)
    service_request = Service.objects.get(id=car_id)
    if form.is_valid():
        car = form.save(commit = False)
        car.owner = request.user
        car.save()
    path = '/' + str(request.user.id) + '/profile/'
    return HttpResponseRedirect(path)
