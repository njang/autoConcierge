from django.conf.urls import url
from .views import main, user, car_owner, shop_owner, service_driver

urlpatterns = [
    url(r'^$', main.index),
    url(r'^signup/$', main.signup),
    url(r'^signup/carowner/$', car_owner.SignUpView.as_view(), name='car_owner_signup'),
    url(r'^signup/shopowner/$', shop_owner.SignUpView.as_view(), name='shop_owner_signup'),
    url(r'^signup/servicedriver/$', service_driver.SignUpView.as_view(), name='service_driver_signup'),
    url(r'^([0-9]+)/profile/$', main.profile, name='profile'),
    url(r'^car/add/$', car_owner.add_car_form, name='add_car_form'),
    url(r'^car/add/post_url/$', car_owner.add_car, name='add_car'),
    url(r'^car/([0-9]+)/$', car_owner.show_car, name='show_car'),
    url(r'^car/([0-9]+)/edit/$', car_owner.edit_car, name='edit_car'),
    url(r'^car/([0-9]+)/edit/update/$', car_owner.update_car, name='update_car'),
    url(r'^car/([0-9]+)/remove/$', car_owner.remove_car, name='remove_car'),
    url(r'^car/([0-9]+)/service/$', car_owner.service_car, name='service_car'),
	url(r'^car/([0-9]+)/service/request/$', car_owner.post_request, name='post_request'),
    url(r'^shop/([0-9]+)/edit/$', shop_owner.edit_shop, name='edit_shop'),
    url(r'^shop/([0-9]+)/edit/update$', shop_owner.update_shop, name='update_shop'),
	url(r'^login/$', user.login_view, name='login'),		# display login page
	url(r'^logout/$', user.logout_view, name='logout'),	# route to logout
]