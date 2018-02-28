from django import forms
from django.db import transaction
from django.utils.translation import ugettext, ugettext_lazy as _
from django.views.generic.edit import UpdateView
from .models import User, CarOwner, ShopOwner, ServiceDriver

class LoginForm(forms.Form):
    email = forms.CharField(label="Email", max_length=254)
    password = forms.CharField(widget=forms.PasswordInput())

class UserCreationForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Re-type Password"),
        widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("email","first_name","last_name")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class CarOwnerSignUpForm(UserCreationForm):
    loc_office = forms.CharField(label='Office location', max_length=100)
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_car_owner = True
        user.save()
        car_owner = CarOwner.objects.create(user=user)
        car_owner.loc_office = self.cleaned_data.get('loc_office')
        car_owner.save()
        return user

class DonorSignUpForm(UserCreationForm):
    location = forms.CharField(max_length=100)
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_donor = True
        user.save()
        donor = Donor.objects.create(user=user)
        donor.location = self.cleaned_data['location']
        donor.save()
        return user

