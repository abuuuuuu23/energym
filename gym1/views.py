from tkinter import Message
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
import requests
from gym1.models import user_account,user_details,trainer_details
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate
# Create your views here.
def index(request):
    # return render(request,'admin.html')
    return render(request,'index.html')

# -----------login section---------------

def login(request):
    return render(request,'login.html')
def login1(request):
    username=request.POST.get('uname')
    password=request.POST.get('pwd')
    user = authenticate(username=username, password=password)
    print(user,"tset1")
    request.session['username']=username
    x = user_account.objects.filter(account_type='user')
    if user is not None and user.is_superuser == 1:
        return redirect('/admin1')
    elif x is not None and user.is_superuser == 0 :
        x = user_account.objects.get(username=user)
        if x.account_type=="user":
            return redirect('/userHome')
        elif x.account_type=="trainer":
            return redirect('/trainerHome')
        else:
            pass
    else:
        return HttpResponse('Invalid response')
    
def adminHome(request):
    return render(request,'admin.html')

def userHome(request):
    a=request.session['username']
    return render(request,'user.html',{'x':a})
def trainerHome(request):
    a=request.session['username']
    return render(request,'trainerHome.html',{'x':a})
    # -----------Login section ended-----------
def create_account(request):
    return render(request,'create_account.html')

def about(request):
    return render(request,'about.html')

def trainers(request):
    return render(request,'trainerForm.html')

def service(request):
    return render(request,'service.html')

def contact(request):
    return render(request,'contact.html')

def create_account2(request):
    a=User()
    b=user_account()
    c=user_details()
    a.username=request.POST.get('username')
    a.email=request.POST.get('email')
    a.first_name=request.POST.get('firstname')
    password=request.POST.get('password')
    a.set_password(password)
    b.username=request.POST.get('username')
    b.firstname=request.POST.get('firstname')
    b.email=request.POST.get('email')
    b.phone=request.POST.get('phone')
    b.account_type='user'
    c.firstname=request.POST.get('firstname')
    c.lastname=request.POST.get('lastname')
    c.gender=request.POST.get('gender')
    c.email=request.POST.get('email')
    c.phone=request.POST.get('phone')
    c.address=request.POST.get('address')
    c.district=request.POST.get('district')
    c.username=request.POST.get('username')
    photo=request.FILES['photo']
    fs= FileSystemStorage()
    filename=fs.save(photo.name,photo) 
    uploaded_file_url=fs.url(filename)
    c.photo=uploaded_file_url
    a.save()
    b.save()
    c.save()
    return render(request,'create_account.html')

def create_trainer2(request):
    a=User()
    b=user_account()
    c=trainer_details()
    a.username=request.POST.get('username')
    a.email=request.POST.get('email')
    a.first_name=request.POST.get('firstname')
    password=request.POST.get('password')
    a.set_password(password)
    b.username=request.POST.get('username')
    b.firstname=request.POST.get('firstname')
    b.email=request.POST.get('email')
    b.phone=request.POST.get('phone')
    b.account_type='trainer'
    c.firstname=request.POST.get('firstname')
    c.lastname=request.POST.get('lastname')
    c.gender=request.POST.get('gender')
    c.email=request.POST.get('email')
    c.phone=request.POST.get('phone')
    c.address=request.POST.get('address')
    c.district=request.POST.get('district')
    c.username=request.POST.get('username')
    photo=request.FILES['photo']
    fs= FileSystemStorage()
    filename=fs.save(photo.name,photo) 
    uploaded_file_url=fs.url(filename)
    c.photo=uploaded_file_url
    c.age=request.POST.get('age')
    c.experience=request.POST.get('experience')
    c.category=request.POST.get('category')
    a.save()
    b.save()
    c.save()
    return render(request,"trainers.html")
