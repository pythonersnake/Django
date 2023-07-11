from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    if request.method == 'POST':
        username=request.POST['username']
        password= request.POST['password']
        csrfmiddlewaretoken = request.POST['csrfmiddlewaretoken']
        print(username, password)
        user = authenticate(request,username=username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request,"You have been logged in")
            return redirect('home')
        else:
            messages.error(request, "Wrong credetinals, please try again")
    return render(request, 'home.html',{})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        print(request.POST)
        #for x,i in request.POST.items():
            #print(x,i)
        first_name= request.POST['first_name']
        last_name=request.POST['last_name']
        user_email = request.POST['email']
        user_password=request.POST['password']
        user = User.objects.create_user(username=user_email,email=user_email,password=user_password,first_name=first_name,last_name=last_name)
        print(user)
    return render(request, 'register.html',{})
