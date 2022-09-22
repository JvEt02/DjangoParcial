"""
importamos la librerias que necesitamos al igual las de django 
"""
from dataclasses import field, fields
from django import forms
from .models import Blog, ContactProfile, Review

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

""""
aqui creamos la clase para el from de  cada informacion que coloca el usurio en el front ends y la recivimos en en
el backend, cada forms tiene los campos de informacion necesaria, por ejemplo nombre, email, author,
el widget se refiere al contenido que va a almacenar los datos suministrado por el usuario.
en la clase meta  la cual utilizamos el model anteriormente creado y en los filds son los datos a almacenar
"""

"""
aqui creamos el Forms de contacto con el model que anteriormente creamos
"""
class ContactForm(forms.ModelForm):

	name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '*Full name..',
			}))
	email = forms.EmailField(max_length=254, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': '*Email..',
			}))
	message = forms.CharField(max_length=1000, required=True, 
		widget=forms.Textarea(attrs={
			'placeholder': '*Message..',
			'rows': 6,
			}))


	class Meta:
		model = ContactProfile
		fields = ('name', 'email', 'message',)

"""
Aqui creamos el forms para la creacion de un nuevo usuario y utilizamos el model de user
"""

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']

"""
Creacion del form para la creacion de los blogs model que anteriormente creamos
"""

class BlogForm(forms.ModelForm):

	author = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '*Author name..',
			}))
	name = forms.CharField(max_length=254, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': '*name..',
			}))
	description = forms.CharField(max_length=254, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': '*Description..',
			}))
	body = forms.CharField(max_length=1000, required=True, 
		widget=forms.Textarea(attrs={
			'placeholder': 'Body info',
			'rows': 6,
			}))
	image = forms.ImageField() 


	class Meta:
		model = Blog
		fields = ['author', 'name', 'description','body','image']

"""
Creacion del form para la creacion de los Reviews model que anteriormente creamos
"""

class ReviewForm(forms.ModelForm):

	author = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '*Author name..',
			}))
	name = forms.CharField(max_length=254, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': '*name..',
			}))
	description = forms.CharField(max_length=254, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': '*Description..',
			}))
	body = forms.CharField(max_length=1000, required=True, 
		widget=forms.Textarea(attrs={
			'placeholder': 'Body info',
			'rows': 6,
			}))
	image = forms.ImageField()


	class Meta:
		model = Review
		fields = ['author', 'name', 'description','body','image']

