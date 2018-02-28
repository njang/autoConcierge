# main_app/urls.py
from django.conf.urls import url
from .views import index, signup, profile_car_owner
from .carOwnerView import CarOwnerSignUpView

urlpatterns = [
    url(r'^$', index),
    url(r'^signup/$', signup),
    url(r'^signup/carowner/$', CarOwnerSignUpView.as_view(), name='car_owner_signup'),
    url(r'^([0-9]+)/car-owner-profile/$', profile_car_owner, name='car_owner_profile'),
]