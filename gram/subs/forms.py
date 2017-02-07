from django import forms
# import Django's UserCreationForm class
from django.contrib.auth.forms import UserCreationForm

# Subclass of UserCreationForm
class SubForm(UserCreationForm):
	# define field of the form
	# form will have username, email, passwords
	# when the form fields are rendered in HTML, the class attribute will be class='form-control'
	email = forms.EmailField(
		required=True, widget=forms.TextInput(attrs={'class': 'form-control' })
	)
	username = forms.CharField(
		widget=forms.TextInput(attrs={'class': 'form-control'})
	)
	password1 = forms.CharField(
		widget=forms.TextInput(attrs={'class': 'form-control', 'type' : 'password'})
	)
	password2 = forms.CharField(
		widget=forms.TextInput(attrs={'class': 'form-control', 'type' : 'password'})
	)