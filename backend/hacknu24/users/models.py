from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from hacknu24.settings import TIME_ZONE

import datetime, pytz

class UserManager(BaseUserManager):
    def create_user(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError(_('The phone number is required'))
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        # extra_fields.setdefault('is_staff', True)
        # extra_fields.setdefault('is_superuser', True)

        # if extra_fields.get('is_staff') is not True:
        #     raise ValueError(_('Superuser must have is_staff=True.'))
        # if extra_fields.get('is_superuser') is not True:
        #     raise ValueError(_('Superuser must have is_superuser=True.'))

        user = self.create_user(phone_number, password, **extra_fields)        
        
        user.is_staff = True
        user.is_superuser = True
        # user.is_superadmin = True
        user.is_active = True
        
        user.save(using = self._db)
        
        return user

class User(AbstractBaseUser):


    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, unique=True)

    is_active = models.BooleanField(default=False)
    is_staff= models.BooleanField(default=False)
    

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone_number

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff


def generate_expiration_time():

    return now() + datetime.timedelta(minutes=5)
    
class UserSMS(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    code = models.CharField(max_length = 8)
    expiry_at = models.DateTimeField(default = generate_expiration_time)

    def is_expired(self):
        return now() > self.expiry_at
    
    def __str__(self) -> str:
        return self.user.phone_number + " - " + self.code
