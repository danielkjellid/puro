from django import forms
from django.forms.utils import ErrorList
from django.utils.html import format_html, format_html_join
from django.utils.safestring import mark_safe
from django.contrib.auth.models import Group

from users.models import User, Note

# Global variables for adding styling to the field inputs
TEXT_INPUT = 'w-full bg-gray-100 border border-gray-300 text-gray-700 rounded-lg py-3 px-4 leading-tight focus:outline-none focus:border-gray-500'
TEXT_AREA = 'w-full bg-gray-100 border border-gray-300 text-gray-700 rounded-lg py-3 px-4 leading-tight focus:outline-none focus:border-gray-500'
CHECKBOX = 'form-checkbox text-gray-800'

# Class for displaying errorlist as divs, and style error messages
class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()
        
    def as_divs(self):
        if not self: return ''
        return mark_safe('<div class="mt-1">%s</div>' % ''.join(['<p class="text-sm text-red-600">%s</p>' % e for e in self]))

# Form for adding a new note
class AddNoteForm(forms.ModelForm):

    # Set form model and form fields
    class Meta:
        model = Note
        fields = ('title', 'content', 'is_sticky')

    # Add styling to the inputs
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': TEXT_INPUT})
        self.fields['content'].widget.attrs.update({'class': TEXT_AREA})
        self.fields['is_sticky'].widget.attrs.update({'class': CHECKBOX})

# Form for editing an existing note
class EditNoteForm(forms.ModelForm):

    # Set form model and form fields
    class Meta:
        model = Note
        fields = ('title', 'content', 'is_sticky')

    # Add styling to the inputs
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': TEXT_INPUT})
        self.fields['content'].widget.attrs.update({'class': TEXT_AREA})
        self.fields['is_sticky'].widget.attrs.update({'class': CHECKBOX})

# Form for deleting an existing note
class DeleteNoteForm(forms.ModelForm):

    # Set form model and empty fields as the form is posted without inputs
    class Meta:
        model = Note
        fields = []

# Form for editing an existing user
class EditUserForm(forms.ModelForm):

    # Set form model and form fields
    class Meta:
        model = User
        fields = (
            'first_name', 
            'last_name', 
            'birth_date', 
            'phone_number', 
            'email', 
            'has_confirmed_email', 
            'address', 
            'zip_code', 
            'zip_place', 
            'disabled_emails', 
            'subscribed_to_newsletter', 
            'allow_personalization', 
            'allow_third_party_personalization', 
            'acquisition_source',
        )

    # Add styling to form inputs
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': TEXT_INPUT})
        self.fields['last_name'].widget.attrs.update({'class': TEXT_INPUT})
        self.fields['birth_date'].widget.attrs.update({'class': TEXT_INPUT})
        self.fields['phone_number'].widget.attrs.update({'class': TEXT_INPUT})
        self.fields['email'].widget.attrs.update({'class': TEXT_INPUT})
        self.fields['has_confirmed_email'].widget.attrs.update({'class': CHECKBOX})
        self.fields['address'].widget.attrs.update({'class': TEXT_INPUT})
        self.fields['zip_code'].widget.attrs.update({'class': TEXT_INPUT})
        self.fields['zip_place'].widget.attrs.update({'class': TEXT_INPUT})
        self.fields['disabled_emails'].widget.attrs.update({'class': CHECKBOX})
        self.fields['subscribed_to_newsletter'].widget.attrs.update({'class': CHECKBOX})
        self.fields['allow_personalization'].widget.attrs.update({'class': CHECKBOX})
        self.fields['allow_third_party_personalization'].widget.attrs.update({'class': CHECKBOX})
        self.fields['acquisition_source'].widget.attrs.update({'class': TEXT_INPUT})

# Form for toggleing the active state of a user
class ToggleUserForm(forms.ModelForm):

    # Set form model and empty fields as the form is posted without inputs
    class Meta:
        model = User
        fields = []

# Form for adding a new user
class AddUserForm(forms.ModelForm):

    #error_css_class = 'border-red-300'

    # Add separate fields to handle email and password, as these has to be checked/cleaned
    email = forms.EmailField()
    password1 = forms.CharField(label = 'Passord', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Bekreft passord', widget = forms.PasswordInput)

    # Set form model and form fields
    class Meta:
        model = User
        fields = (
            'first_name', 
            'last_name',
            'password1',
            'password2',
            'birth_date', 
            'phone_number', 
            'email', 
            'has_confirmed_email', 
            'address', 
            'zip_code', 
            'zip_place', 
            'disabled_emails', 
            'subscribed_to_newsletter', 
            'allow_personalization', 
            'allow_third_party_personalization', 
            'acquisition_source',
        )

    # Method for cleaning ang checking email
    def clean_email(self):

        # Get data from input field
        email = self.cleaned_data.get('email')

        # Normalize email by lowercasing the domain part
        def normalize_email(email):
            email = email or ''
            try:
                email_name, domain_part = email.strip().rsplit('@', 1)
            except ValueError:
                pass
            else:
                email = email_name + '@' + domain_part.lower()
            return email

        # Query the email
        query = User.objects.filter(email = email)

        # If the email already exists, raise ValidationError
        if query.exists():
            raise forms.ValidationError('E-posten er allerede i bruk!')

        return normalize_email(email)

    # Method for checking if the two password entries match
    def clean_password2(self):

        # Get data from input fields
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        # Check if password1 and password2 match
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passordene stemmer ikke overens")
        return password2

    # Method for saving the user
    def save(self, commit = True):

        # Save user
        user = super().save(commit = False)

        # Set password in hashed format
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user

    # Add styling to field inputs
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': TEXT_INPUT})
        self.fields['last_name'].widget.attrs.update({'class': TEXT_INPUT})
        self.fields['password1'].widget.attrs.update({'class': TEXT_INPUT})
        self.fields['password2'].widget.attrs.update({'class': TEXT_INPUT})
        self.fields['birth_date'].widget.attrs.update({'class': TEXT_INPUT})
        self.fields['phone_number'].widget.attrs.update({'class': TEXT_INPUT})
        self.fields['email'].widget.attrs.update({'class': TEXT_INPUT})
        self.fields['has_confirmed_email'].widget.attrs.update({'class': CHECKBOX})
        self.fields['address'].widget.attrs.update({'class': TEXT_INPUT})
        self.fields['zip_code'].widget.attrs.update({'class': TEXT_INPUT})
        self.fields['zip_place'].widget.attrs.update({'class': TEXT_INPUT})
        self.fields['disabled_emails'].widget.attrs.update({'class': CHECKBOX})
        self.fields['subscribed_to_newsletter'].widget.attrs.update({'class': CHECKBOX})
        self.fields['allow_personalization'].widget.attrs.update({'class': CHECKBOX})
        self.fields['allow_third_party_personalization'].widget.attrs.update({'class': CHECKBOX})
        self.fields['acquisition_source'].widget.attrs.update({'class': TEXT_INPUT})