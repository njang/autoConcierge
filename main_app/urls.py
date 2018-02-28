# main_app/urls.py
from django.conf.urls import url
# from .views import index, signup, profile_car_owner
# from .carOwnerView import CarOwnerSignUpView
from .views import main, car_owner

urlpatterns = [
    url(r'^$', main.index),
    url(r'^signup/$', main.signup),
    url(r'^signup/carowner/$', car_owner.CarOwnerSignUpView.as_view(), name='car_owner_signup'),
    url(r'^([0-9]+)/car-owner-profile/$', main.profile_car_owner, name='car_owner_profile'),
]