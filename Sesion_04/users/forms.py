"""Users app forms"""

from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class UserForm(forms.Form):
    """User form"""
    username = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirmation = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        """Checks if username is unique"""
        username = self.cleaned_data.get('username')
        username_exists = User.objects.filter(username=username).exists()

        if username_exists:
            raise forms.ValidationError("Este username ya está en uso")

        return username

    def clean(self):
        """Checks if passwords matches"""
        data = self.cleaned_data
        password = data.get('password')
        password_confirmation = data.get('password_confirmation')

        if password != password_confirmation:
            raise forms.ValidationError("Las contraseñas no coinciden")

        return data

    def save(self):
        """Creates a new user"""
        data = self.cleaned_data
        data.pop('password_confirmation') # Con este comando quitamos el campo del diccionario
        return User.objects.create_user(**data) ## Con el doble * desplegamos toda la información de la forma en el diccionario