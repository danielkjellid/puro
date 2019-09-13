from django import forms

from users.models import User, Note

class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('content', 'is_sticky')

class UserEditForm(forms.ModelForm):
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
            'is_active'
        )

class UserToggleForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('is_active',)