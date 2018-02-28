from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, ListView, UpdateView
from main_app.forms import ServiceDriverSignUpForm
from main_app.models import User, ServiceDriver
from django.contrib.auth import login

class SignUpView(CreateView):
    model = User
    form_class = ServiceDriverSignUpForm
    template_name = 'registration/service_driver.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        path = '/' + str(user.id) + '/service-driver-profile/'
        return redirect(path)