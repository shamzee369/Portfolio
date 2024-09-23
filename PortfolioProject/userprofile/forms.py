from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'skills', 'contact', 'profile_image', 'user_type']  # Include 'user_type'
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter your bio'}),
            'skills': forms.TextInput(attrs={'placeholder': 'Enter your skills'}),
            'contact': forms.TextInput(attrs={'placeholder': 'Enter your contact details'}),
            'user_type': forms.HiddenInput(),  # Hide 'user_type' in the form
        }

def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        # Force the 'user_type' field value to 'user'
        self.fields['user_type'].initial = 'user'

def save(self, commit=True):
        user_profile = super().save(commit=False)
        user_profile.user_type = 'user'  # Force the user_type to 'user'
        if commit:
            user_profile.save()
        return user_profile


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

