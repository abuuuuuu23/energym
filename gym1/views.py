from tkinter import Message
from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
# import requests
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
    print(username,"test111",password)
    user = authenticate(username=username, password=password)
    print(user,"tset1")
    request.session['username']=username
    if user is not None and user.is_superuser == 1:
        return redirect('/adminHome')
    elif user is not None and user.is_superuser == 0:
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
    b=user_details.objects.get(username=a)
    return render(request,'user.html',{'x':a ,'y':b})
def trainerHome(request):
    a=request.session['username']
    b=trainer_details.objects.get(username=a)
    return render(request,'trainerHome.html',{'x':a,'y':b})
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
    print(password,"test3")
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
    return redirect('/adminHome/')

def view_trainer(request):
    a=trainer_details.objects.all()
    return render(request,'view_trainer.html',{'data':a})

def update_trainer(request,id):
    b=trainer_details.objects.get(id=id)
    return render(request,'update_trainer.html',{'data':b})


def update_trainer2(request,id):
    a=trainer_details.objects.get(id=id)
    try:
        a.firstname=request.POST.get('firstname')
        a.lastname=request.POST.get('lastname')
        a.email=request.POST.get('email')
        a.phone=request.POST.get('phone')
        a.address=request.POST.get('address')
        a.district=request.POST.get('district')
        photo=request.FILES['photo']
        fs= FileSystemStorage()
        filename=fs.save(photo.name,photo) 
        uploaded_file_url=fs.url(filename)
        a.photo=uploaded_file_url
    
        a.age=request.POST.get('age')
        a.experience=request.POST.get('experience')
        a.category=request.POST.get('category')
        a.save()
    except:
        a.firstname=request.POST.get('firstname')
        a.lastname=request.POST.get('lastname')
        a.email=request.POST.get('email')
        a.phone=request.POST.get('phone')
        a.address=request.POST.get('address')
        a.district=request.POST.get('district')
        a.age=request.POST.get('age')
        a.experience=request.POST.get('experience')
        a.category=request.POST.get('category')
        a.save()    
    return redirect('/view_trainer/')

def view_user(request):
    a=request.session['username']
    b=user_details.objects.get(username=a)
    return render(request,'view_user.html',{'data':b})

def delete_trainer(request):
    a=trainer_details.objects.all()
    return render(request,'delete_trainer.html',{'data':a})
def delete_trainer1(request,id):
    a=trainer_details.objects.get(id=id)
    b=User.objects.get(username=a.username)
    c=user_account.objects.get(username=a.username)

    a.delete()
    b.delete()
    c.delete() 
    return redirect('/delete_trainer/')

def trainer_d(request,id):
    # a=request.session['username']
    b=trainer_details.objects.get(id=id)
    return render(request,'trainer_d.html',{'data':b})

def logout(request):
    auth.logout(request)
    return redirect("/")

def update_user(request):
    a=request.session['username']
    b=user_details.objects.get(username=a)
    return render(request,'update_user.html',{'data':b})

def update_user2(request):
    a=request.session['username']
    b=user_details.objects.get(username=b)
    try:
        a.firstname=request.POST.get('firstname')
        a.lastname=request.POST.get('lastname')
        a.email=request.POST.get('email')
        a.phone=request.POST.get('phone')
        a.address=request.POST.get('address')
        a.district=request.POST.get('district')
        photo=request.FILES['photo']
        fs= FileSystemStorage()
        filename=fs.save(photo.name,photo) 
        uploaded_file_url=fs.url(filename)
        a.photo=uploaded_file_url
        a.save()
    except:
        a.firstname=request.POST.get('firstname')
        a.lastname=request.POST.get('lastname')
        a.email=request.POST.get('email')
        a.phone=request.POST.get('phone')
        a.address=request.POST.get('address')
        a.district=request.POST.get('district')
        a.save()    
    return redirect('/view_user/')

# def delete_user(request):
#     a=request.session['username']
#     b=user_details.objects.get(username=a)
#     return render(request,'view_user.html',{'data':b})
def delete_user(request):
    a=request.session['username']
    b=user_details.objects.get(usename=a)
    c=User.objects.get(username=a)
    d=user_account.objects.get(username=a)

    b.delete()
    c.delete() 
    d.delete()
    return redirect('/''/')