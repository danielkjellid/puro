import phonenumbers

from django.db import models
from django.utils import timezone
from django.utils.text import get_text_list
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    BaseUserManager, 
    AbstractBaseUser,
    Group,
    PermissionsMixin
)
from phonenumber_field.modelfields import PhoneNumberField

# Manager for user, extending BaseUserManager
class UserManager(BaseUserManager):

    # Method for creating normal users with required fields
    def create_user(self, email, birth_date, phone_number, password=None):
        
        # Check if email is defined, if not, raise ValueError
        if not email:
            raise ValueError('Brukere må ha en e-postadresse')
        
        # Creating the user
        user = self.model(

            # Normalize email by lowercasing the domain part
            email = self.normalize_email(email),

            # Set birth date and phone number to inputs
            birth_date = birth_date,
            phone_number = phone_number,
        )

        # Set password to input
        user.set_password(password)

        # Save user to the database
        user.save(using = self._db)
        return user

    # Method for creating superusers
    def create_superuser(self, email, birth_date, phone_number, password):
        
        # Use the create_user method to define base and add inputs to fields
        user = self.create_user(
            email,
            password = password,
            birth_date = birth_date,
            phone_number = phone_number,
        )

        # In adition to adding a base user, set the superuser to staff and superuser
        user.is_staff = True
        user.is_superuser = True

        # Save user to the database
        user.save(using = self._db)
        return user

# User model which inherits AbstractBaseuser. AbstractBaseUser provides the core implementation of a user model.
class User(AbstractBaseUser, PermissionsMixin):

    # Set model fields
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
        related_name = 'user_roles',
        related_query_name = 'user_roles',
    )

    # Add the user model to UserManager
    objects = UserManager()

    # Set username field to email instead of username
    USERNAME_FIELD = 'email'

    # Set required fields. These fields with create problems if not defined
    REQUIRED_FIELDS = ['birth_date', 'phone_number']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        permissions = (
            ('has_users_export', 'Can export users list'),
            ('has_users_access', 'Can list and search users'),
            ('has_user_add', 'Allows the user to add new users'),
            ('has_user_management', 'Can edit user details'),
            ('has_user_export', 'Can export user details'),
            ('has_user_hijack', 'Can log in as user'),
            ('has_user_high_level_management', 'Can toggle users active state'),
        )

    # Define user identifier
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    # Method for checking if the user has a permission, returns True if the user has each of the specified permissions
    def has_perm(self, perm, obj=None):
        return True

    # Method for checking if the user has package permissions, returns True if the user has any permissions in the given package
    def has_module_perms(self, backend):
        return True

    # Method for getting the full name of a user
    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    # Method for getting the first name of a user
    def get_short_name(self):
        return self.first_name

    # Method for getting the full address formatted of a user
    def get_full_address(self):
        full_address = '%s, %s %s' % (self.address, self.zip_code, self.zip_place)
        return full_address.strip()

    # Method for sending an email to the user
    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    # Method for formatting phonenumbers
    def formatted_phone(self, country = None):
        parsed = phonenumbers.parse(self.phone_number, country)
        return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

    # Method for getting initials of a user.
    def get_initials(self):
        return self.first_name[0] + self.last_name[0]

# Note model
class Note(models.Model):

    # Model fields
    title = models.CharField(verbose_name='Tittel', max_length = 255, unique = False)
    is_sticky = models.BooleanField(default = False)
    content = models.TextField()
    date_edited = models.DateTimeField(default = timezone.now)
    user = models.ForeignKey(User, related_name = 'user_noted', on_delete = models.CASCADE)
    author = models.ForeignKey(User, related_name = 'note_by', on_delete = models.CASCADE)

    # Meta class setting name and plural name.
    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
        permissions = (
            ('has_note_view', 'User can view notes'),
            ('has_note_add', 'User can add notes'),
            ('has_note_edit', 'User can edit notes'),
            ('has_note_delete', 'User can delete notes'),
        )

    # Define note identifier
    def __str__(self):
        return self.content




