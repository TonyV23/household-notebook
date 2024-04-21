from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms

from app.models import Quartier
from app.models import UserProfile

class UserForm(UserCreationForm):

    quartier = forms.ModelChoiceField(queryset=Quartier.objects.all())
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
            'quartier',
        ]

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "Les mots de passe ne correspondent pas.")

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password1']
        user.set_password(password)
        if commit:
            user.save()
            user_profile = UserProfile(user=user, quartier=self.cleaned_data['quartier'])
            user_profile.save()
        return user


class UserEditInfoForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
        ]