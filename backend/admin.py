from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from backend.models import Notes, Supplier
from users.models import User

class UserCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all req. fields, plus a repeated password.
    """

    password1 = forms.CharField(label = 'Passord', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Bekreft passord', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'birth_date')

    def clean_password2(self):
        # Password match check
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passordene stemmer ikke overens")
        return password2

    def save(self, commit = True):
        # Save password in a hashed format
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    """
    Form for updating users
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            'first_name', 
            'last_name', 
            'birth_date', 
            'phone_number',
            'email',
            'has_confirmed_email',
            'password',
            'address',
            'zip_code',
            'zip_place',
            'subscribed_to_newsletter',
            'allow_personalization',
            'allow_third_party_personalization',
            'acquisition_source',
            'date_joined',
            'last_login',
            'is_active',
            'is_staff',
            'is_superuser',
            'roles'
        )

        def clean_password(self):
            # Regardless of what the user provides, return the initial value.
            # This is done here, because the field does not have access to initial value
            return self.initial["password"]

class UserAdmin(BaseUserAdmin):
    # Forms to add and change users
    user_change_form = UserChangeForm
    user_add_form = UserCreationForm

    # Fields used in displaying the user model

    list_display = (
        'first_name', 
        'last_name', 
        'email', 
        'is_active', 
        'is_staff', 
        'is_superuser', 
    )
    list_filter = (
        'is_active', 
        'is_staff', 
        'is_superuser', 
        'roles'
    )
    fieldsets = (
        (
            'Personlig', 
            {
                'fields': (
                    'first_name', 
                    'last_name', 
                    'birth_date', 
                    'date_joined', 
                    'last_login', 
                    'password'
                )
            }
        ),
        (
            'Kontakt', 
            {
                'fields': (
                    'phone_number', 
                    'email', 
                    'has_confirmed_email', 
                    'address', 
                    'zip_code', 
                    'zip_place'
                )
            }
        ),
        (
            'Markedsføring', 
            {
                'fields': (
                    'subscribed_to_newsletter', 
                    'allow_personalization', 
                    'allow_third_party_personalization', 
                    'acquisition_source'
                )
            }
        ),
        (
            'Rettigheter', 
            {
                'fields': (
                    'is_active', 
                    'is_staff', 
                    'is_superuser', 
                    'roles'
                )
            }
        )
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'birth_date', 'phone_number','password1', 'password2')
        }),
    )

    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('first_name', 'last_name', 'email')
    filter_horizontal = ()

admin.site.register(User, UserAdmin)

class NoteAdmin(admin.ModelAdmin):
    list_display = [
        'is_sticky',
        'content',
        'date_edited',
        'user',
        'author'
    ]

admin.site.register(Notes, NoteAdmin)

class SupplierAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'contact',
        'contact_email',
        'contact_phone',
        'is_active'
    ]

admin.site.register(Supplier, SupplierAdmin)