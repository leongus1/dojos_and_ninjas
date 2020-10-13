from django.shortcuts import render, redirect, HttpResponse
from .models import dojos, ninjas
from django.db import models

# Create your views here.
def index(request):
    context = {
        'dojos': dojos.objects.all(),
        'ninjas': ninjas.objects.all(),
    }
    return render(request, 'index.html',context)

def add_dojo(request):
    dojos.objects.create(name=request.POST['name'], city=request.POST['city'] , state=request.POST['state'], desc="default")
    return redirect('/')

def add_ninja(request):
    # dojo=request.POST['dojo']
    ninjas.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], dojo=dojos.objects.get(id=request.POST['dojo']) )
    return redirect('/')

def delete(request, id):
    thisDojo = dojos.objects.get(id=id)
    thisDojo.delete()
    return redirect('/')
    # return HttpResponse('delete path working')