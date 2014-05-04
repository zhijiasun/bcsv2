from django.shortcuts import render,render_to_response

# Create your views here.

def index(request):
	c = {}
	return render_to_response('index.html',c)