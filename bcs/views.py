from django.shortcuts import render,render_to_response,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User

# Create your views here.

def index(request):
	c = {}
	print 'aa'
	if request.user:
		print request.user.username
		print 'bbb'
	else:
		print 'no user login'

	return render(request,'index.html')	

def logout1(request):
	logout(request)
	return redirect('/bcs/index/')

