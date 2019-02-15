from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app.user.validators import validateEmail, validatePassword


class UserForm(UserCreationForm):

	username = forms.CharField(max_length=40, label='Usuario', widget=forms.TextInput(attrs={'autocomplete':'off', 'style': 'width:300px;', 'class':'form-control'}))
	first_name = forms.CharField(max_length=40, label='Nombre', widget=forms.TextInput(attrs={'autocomplete':'off', 'style': 'width:300px;', 'class':'form-control'}))
	last_name = forms.CharField(max_length=60, label='Apellidos', widget=forms.TextInput(attrs={'autocomplete':'off', 'style': 'width:300px;', 'class':'form-control'}))
	email = forms.CharField(label='Correo Electronico', widget=forms.TextInput(attrs={'autocomplete':'off', 'style': 'width:300px;', 'class':'form-control'}), validators=[validateEmail])
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'style': 'width:300px;', 'class':'form-control'}), validators=[validatePassword])
	password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={'style': 'width:300px;', 'class':'form-control'}))

	class Meta:

		model = User

		fields = ('username', 'first_name', 'last_name', 'email')
