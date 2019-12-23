from django import forms

from users.models import User, Note

TEXT_INPUT = 'w-full bg-gray-100 border border-gray-300 text-gray-700 rounded-lg py-3 px-4 leading-tight focus:outline-none focus:border-gray-500'
TEXT_AREA = 'w-full bg-gray-100 border border-gray-300 text-gray-700 rounded-lg py-3 px-4 leading-tight focus:outline-none focus:border-gray-500'
CHECKBOX = 'form-checkbox text-gray-800'

class AddNoteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': TEXT_INPUT})
        self.fields['content'].widget.attrs.update({'class': TEXT_AREA})
        self.fields['is_sticky'].widget.attrs.update({'class': CHECKBOX})

    class Meta:
        model = Note
        fields = ('title', 'content', 'is_sticky')

class EditNoteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': TEXT_INPUT})
        self.fields['content'].widget.attrs.update({'class': TEXT_AREA})
        self.fields['is_sticky'].widget.attrs.update({'class': CHECKBOX})

    class Meta:
        model = Note
        fields = ('title', 'content', 'is_sticky')

class DeleteNoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = []

class EditUserForm(forms.ModelForm):

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



