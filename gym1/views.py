from django.shortcuts import render
from django.contrib.auth.models import User
from gym1.models import user_account,user_details,trainer_account,trainer_details
from django.core.files.storage import FileSystemStorage
# Create your views here.
def index(request):
    # return render(request,'admin.html')
    return render(request,'index.html')

# def admin(request):
#     return render(request,'admin.html')

# def user(request):
#     return render(request,'user.html')

def login(request):
    return render(request,'login.html')

def create_account(request):
    return render(request,'create_account.html')

def about(request):
    return render(request,'about.html')

def trainers(request):
    return render(request,'trainers.html')

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

