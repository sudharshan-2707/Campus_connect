from django.shortcuts import render
from django.contrib.auth import get_user_model
from celery import shared_task 
from django.core.mail import send_mail
from project import settings
from django.shortcuts import render,redirect
from .models import Register,Event
from .tasks import send_mail_func

def register(request):
    return render(request,'register.html')

def home(request):
    return render(request,'home.html')

def event(request):
    return render(request,'event.html')

def aboutus(request):
    return render(request,'aboutus.html')

def course(request):
    return render(request,'courses.html')

def facility(request):
    return render(request,'Facilities.html')

def plac(request):
    return render(request,'placement.html')

def thank(request):
    return render(request,'thank.html')

def eventdet(request):
    if request.method=="POST" :
        reg = Register()
        reg.user_name = request.POST.get("name")
        reg.email = request.POST.get("email")
        reg.phone = request.POST.get("phone")
        reg.save()
        email=request.POST.get("email")
       
        c= send_mail_func(email)
        print(c)
        return redirect("/thank")

    return render(request,'eventdetails.html')

def dispevent(request):
     data=Event.objects.all()
     return render(request,'dispevent.html',{'data': data})

def dispeventdet(request,name):
    data=Event.objects.filter(name=name)
    return render(request,'eventdetails.html',{'data': data})
# Create your views here.
