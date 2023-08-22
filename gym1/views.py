from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def create_account(request):
    return render(request,'create_account.html')

def about(request):
    return render(request,'about.html')