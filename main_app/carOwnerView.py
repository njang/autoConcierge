from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, ListView, UpdateView
from .forms import CarOwnerSignUpForm
from .models import User, CarOwner
from django.contrib.auth import login

class CarOwnerSignUpView(CreateView):
    model = User
    form_class = CarOwnerSignUpForm
    template_name = 'registration/car_owner.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        path = '/' + str(user.id) + '/car-owner-profile/'
        return redirect(path)