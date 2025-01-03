from datetime import datetime

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from taggit.forms import TagField, TagWidget

from .models import UserProfile, Post, Comment


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True,
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


class InvalidDataException(forms.ValidationError):
    pass


class CreatePostForm(forms.ModelForm):
    tags = TagField()

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

        widgets = {
            'tags': TagWidget(),
        }
 # def __init__(self, *args, **kwargs):
 #     super().__init__(*args, **kwargs)
 #     self.fields['author'].queryset = User.objects.filter(
 #         id=kwargs.pop('user_id', None))
 #     if not self.instance.pk:
 #         self.initial['author'] = self.fields['author'].queryset.first()

    def save(self, commit=True):
        instance = super().save(commit=False)
        # ensure a user is present
        if not self.request.user:
            raise InvalidDataException('No user provided')
        instance.author = self.request.user

        # create new tags if not already in DB
        tags = self.cleaned_data['tags']
        # for tag in tags:
        #     if not tag.pk:
        #         tag.save()
        instance.tags.add(*tags)

        if commit:
            instance.save()
        return instance


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image', "email"]


class CommentForm(forms.ModelForm):

    def save(self, commit=True):
        instance = super().save(commit=False)

        if not self.request.user:
            raise InvalidDataException('No user provided')
        instance.user = self.request.user

        if commit:
            instance.save()
        return instance

    class Meta:
        model = Comment
        fields = ['content', ]
