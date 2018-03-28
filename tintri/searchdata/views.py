import json
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render



# Create your views here.

def index(request):
	return render(request, 'searchdata/index.html')

def index1(request):
	return render(request, 'searchdata/index1.html')

def search_quarantine(request):
	return render(request, 'searchdata/search_quarantine.html')

def unquarantine_factory(request):
	return render(request, 'searchdata/unquarantine_factory.html')

def machines(request):
	machines = json.load(open('./machines.json','r'))
	return HttpResponse(json.dumps({"data":machines}))