from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
# from phonenumber_field.modelfields import PhoneNumberField

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    name_first = models.CharField(max_length=50)
    name_last = models.CharField(max_length=50)
    is_car_owner = models.BooleanField(default=False)
    is_shop_owner = models.BooleanField(default=False)
    is_service_driver = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

class CarOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    loc_office = models.CharField(max_length=100)
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='car_owner')
    car_year = models.IntegerField(default=2010)
    car_make = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_model_trim = models.CharField(max_length=100)
    car_color = models.CharField(max_length=100)
    car_license = models.CharField(max_length=100)
    loc_parking = models.CharField(max_length=100)

    def __str__(self):
        return str(self.owner.first_name) + '\'s ' + str(self.car_year) + ' ' + str(self.car_make) + ' ' + str(self.car_model)

class Service(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='owner_car')
    car = models.ForeignKey(Car, on_delete=models.PROTECT, related_name='car')
    description = models.CharField(max_length=100)
    date = models.DateField(null=True)
    shop = models.ForeignKey(User, on_delete=models.PROTECT, related_name='owner_shop')
    def __str__(self):
        return self.description
    
class ShopOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    shop_name = models.CharField(max_length=100)
    address_street = models.CharField(max_length=100)
    address_gps_lat = models.DecimalField(max_digits=10, decimal_places=6, default=0)
    address_gps_lng = models.DecimalField(max_digits=10, decimal_places=6, default=0)
    phone_number = models.CharField(max_length=100)
    def __str__(self):
        return self.shop_name

class ServiceDriver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_over_21 = models.BooleanField(default=False)
    is_gpa_over3 = models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name