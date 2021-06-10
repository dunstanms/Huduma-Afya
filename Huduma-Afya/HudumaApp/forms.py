from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Patient Doctor, Receptionist, Appointment



class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        exclude = ('admin',)


class ReceptionistForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user', 'Doctor')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', )
