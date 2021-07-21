from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = (
            'user',
            'role',
        )
        

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes. Remove auto-generated
        labels and set autofocus on first field
        """
        super(UserProfileForm, self).__init__(*args, **kwargs)
        placeholders = {
            'profile_phone_number': 'Phone Number',
            'profile_street_address1': 'Street Address1',
            'profile_street_address2': 'Street Address2',
            'profile_town_or_city': 'Town or City',
            'profile_county': 'County or State',
            'profile_postcode': 'Postcode',
            'role': 'User Role',       
        }

        self.fields['profile_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'profile_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False
