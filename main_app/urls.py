from django.conf.urls import url
from .views import main, car_owner, shop_owner, service_driver, user

urlpatterns = [
    url(r'^$', main.index),
    url(r'^signup/$', main.signup),
    url(r'^signup/carowner/$', car_owner.SignUpView.as_view(), name='car_owner_signup'),
    url(r'^signup/shopowner/$', shop_owner.SignUpView.as_view(), name='shop_owner_signup'),
    url(r'^signup/servicedriver/$', service_driver.SignUpView.as_view(), name='service_driver_signup'),
    url(r'^([0-9]+)/profile/$', main.profile, name='profile'),
    url(r'^car/add/$', main.add_car_form, name='add_car_form'),
    url(r'^car/add/post_url/$', main.add_car, name='add_car'),
    url(r'^car/([0-9]+)/$', main.show_car, name='show_car'),
    url(r'^car/([0-9]+)/edit/$', main.edit_car, name='edit_car'),
    url(r'^car/([0-9]+)/edit/update/$', main.update_car, name='update_car'),
	url(r'^car/([0-9]+)/remove/$', main.remove_car, name='remove_car'),
	url(r'^login/$', user.login_view, name='login'),		# display login page
	url(r'^logout/$', user.logout_view, name='logout'),	# route to logout
]