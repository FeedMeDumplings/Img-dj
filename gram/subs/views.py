from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse

# Create your views here.

from .forms import SubForm

def sub_new(request, template='subs/sub_new.html'):
	# check HTTP method
	if request.method == 'POST':
		# form data accessed at request.POST
		form = SubForm(request.POST)
		# form validation - validate user input to check if it matches
		if form.is_valid():
			# Unpack form values
			# creating objects from user input data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			email = form.cleaned_data['email']
			# Create the user record - an instance
			user = User(username=username, email=email)
			user.set_password(password)
			# save the user record to the database
			user.save()
			# Create Sub Record
			# if it succeeds in creating a new user database, page will be directed to 'post_list'
			# if it fails then the user will be directed to login page
			new_u = authenticate(username=username, password=password)
			if new_u is not None:
				if new_u.is_active:
					login(request, new_u)
					return HttpResponseRedirect(reverse('post_list'))
				else:
					return HttpResponseRedirect(
						reverse('django.contrib.auth.views.login')
					)
			else:
				return HttpResponseRedirect(reverse('sub_new'))
	else:
		# if user is requesting a sub form for the first time
		form = SubForm()
	return render(request, template, { 'form' : form })

