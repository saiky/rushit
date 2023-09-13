from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

import datetime

# import the logging library
import logging

logger = logging.getLogger(__name__)

# Create your login views here.
def LoginView(request):
	if request.user.is_authenticated:
		return  redirect("/")
	if request.method == "POST":
		logger.debug('Loginpage was accessed at '+str(datetime.datetime.now())+' hours!')
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(request, username=username, password=password)
		if user is None:
			context = {"error":"You enter invalid username or password"} 
			return render(request, "accounts/login.html", context)
		elif user is not None:
			login(request, user)
			return redirect("/")			
	print("hello I am here")
	return render(request, "accounts/login.html", {})

# Create your logout views here.
def IndexView(request):
	return render(request, "accounts/index.html", {})

# Create your logout views here.
def LogoutView(request):
	logout(request)
	return redirect("login")


# Create your register views here.
def RegisterView(request):

	return render(request, "accounts/register.html", {})