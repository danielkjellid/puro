from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    BaseUserManager, 
    AbstractBaseUser,
    Group
)
from phone_field import PhoneField
from users.models import User

class Notes(models.Model):
    is_sticky = models.BooleanField(default = False)
    content = models.TextField()
    date_edited = models.DateTimeField(default = timezone.now)
    user = models.ForeignKey(User, related_name = 'User', on_delete = models.CASCADE)
    author = models.ForeignKey(User, related_name = 'Author', on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'

class Supplier(models.Model):
    name = models.CharField(max_length = 255)
    contact = models.CharField(max_length = 255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length = 31)
    is_active = models.BooleanField()

    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'