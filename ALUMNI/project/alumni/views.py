from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    if request.method=="POST":
        a=request.POST.get('username')
        b=request.POST.get('password')
        obj=authenticate(username=a,password=b)
        if obj:
            login(request,obj)
        else:
            return redirect('homepage')
    return render(request,'login.html')

def register(request):






    
    return render(request,'register.html')

def profile(request):
    return render(request,'profile.html')

def logout(request):
    return render(request,'logout.html')

def delete(request):
    return render(request,'delete.html')

def update(request):
    return render(request,'update.html')

def about(request):
    return render(request,'about.html')

def dedicated(request):
    return render(request,'dedicated.html')

def contact(request):
    return render(request,'contact.html')

def staff(request):
    return render(request,'staff.html')





