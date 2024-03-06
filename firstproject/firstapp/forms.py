# forms.py
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'surname', 'fathername', 'address', 'fincode', 'register_type','phone', 'email', 'desc','attachment']


    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        # Customize choices for the verification_code field
        self.fields['register_type'].widget = forms.Select(choices=self.get_verification_code_choices())

    # Define choices for the verification_code fieldchange it 
    def get_verification_code_choices(self):
        # Define your choices here, for example:
        return [
            ('İnvestor', 'İnvestor'),
            ('Emitent', 'Emitent'),
            ('İnvestisiya şirkəti', ' İnvestisiya şirkəti'),
            # Add more choices as needed
        ]
