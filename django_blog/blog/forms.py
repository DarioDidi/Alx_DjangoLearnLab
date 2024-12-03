from django import forms
from django.forms import EmailField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile

class UserCreationForm(UserCreationForm):
    email = EmailField(label="Email", required=True,
                       help_text=("Please enter email"))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            return user
        

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image', "email"]

