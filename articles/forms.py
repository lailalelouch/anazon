from django import forms
from .models import Book
from django.contrib.auth.models import User

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		exclude = ["sold_by"]


class UpdateBookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ["description", "price"]


class RegistrationForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username", "password"]
		widgets = {
			"password" : forms.PasswordInput()
		}


class LoginForm(forms.Form):
	username = forms.CharField(max_length=150)
	password = forms.CharField(max_length=150, widget=forms.PasswordInput())
