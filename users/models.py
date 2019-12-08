import phonenumbers

from django.db import models
from django.utils import timezone
from django.utils.text import get_text_list
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    BaseUserManager, 
    AbstractBaseUser,
    Group
)
from phonenumber_field.modelfields import PhoneNumberField

class UserManager(BaseUserManager):
    def create_user(self, email, birth_date, phone_number, password=None):
        if not email:
            raise ValueError('Brukere må ha en e-postadresse')

        user = self.model(
            email = self.normalize_email(email),
            birth_date = birth_date,
            phone_number = phone_number,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, birth_date, phone_number, password):
        user = self.create_user(
            email,
            password = password,
            birth_date = birth_date,
            phone_number = phone_number,
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class User(AbstractBaseUser):
    first_name = models.CharField(
        verbose_name = 'fornavn',
        max_length = 255,
        unique = False,
    )
    last_name = models.CharField(
        verbose_name = 'etternavn',
        max_length = 255,
        unique = False,
    )
    birth_date = models.DateField(
        verbose_name = "fødselsdag",
    )
    phone_number = models.CharField(
        max_length = 255
    )
    email = models.EmailField(
        verbose_name = 'e-post',
        max_length = 255,
        unique = True,
    )
    has_confirmed_email = models.BooleanField(
        default = False
    )
    address = models.CharField(
        verbose_name = 'adresse',
        max_length = 255,
        unique = False,
    )
    zip_code = models.CharField(
        verbose_name = 'postkode',
        max_length = 255,
        unique = False,
    )
    zip_place = models.CharField(
        verbose_name = 'poststed',
        max_length = 255,
        unique = False,
    )
    disabled_emails = models.BooleanField(
        default = False
    )
    subscribed_to_newsletter = models.BooleanField(
        default = True
    )
    allow_personalization = models.BooleanField(
        default = True
    )
    allow_third_party_personalization = models.BooleanField(
        default = True
    )
    acquisition_source = models.CharField(
        verbose_name = 'Opprettet gjennom',
        blank = True,
        max_length = 255,
        unique = False,
    )
    date_joined = models.DateTimeField(
        _('date_joined'),
        default = timezone.now
    )
    is_active = models.BooleanField(
        default = True
    )
    is_staff = models.BooleanField(
        default = False
    )
    is_superuser = models.BooleanField(
        default = False
    )
    roles = models.ManyToManyField(
        Group,
        verbose_name = _('roles'),
        blank = True,
        related_name = 'user_set',
        related_query_name = 'user',
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['birth_date', 'phone_number']

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, backend):
        return True

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def get_full_address(self):
        full_address = '%s, %s %s' % (self.address, self.zip_code, self.zip_place)
        return full_address.strip()

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def formatted_phone(self, country = None):
        parsed = phonenumbers.parse(self.phone_number, country)
        return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

    def get_initials(self):
        return self.first_name[0] + self.last_name[0]

class Note(models.Model):
    is_sticky = models.BooleanField(default = False)
    content = models.TextField()
    date_edited = models.DateTimeField(default = timezone.now)
    user = models.ForeignKey(User, related_name = 'user_noted', on_delete = models.CASCADE)
    author = models.ForeignKey(User, related_name = 'note_by', on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'

    def __str__(self):
        return self.content




