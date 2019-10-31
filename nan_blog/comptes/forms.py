from django import forms
from django.contrib.auth.models import User
from .models import Profile


# On veut modifier les valeurs des Users enregistrésds la BD
class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email']
    

# On met modifier aussi en memetant l'image de l'user si l on veut 
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['imageprofile']