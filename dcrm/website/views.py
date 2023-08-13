from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignUpForm
from .models import Record
from .forms import AddRecordForm
# Create your views here.
def home(request):
    records = Record.objects.all()
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
    return render(request, 'home.html',{'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')

# def register_user(request):
#     if request.method == 'POST':
#         print(request.POST)
#         #for x,i in request.POST.items():
#             #print(x,i)
#         first_name= request.POST['first_name']
#         last_name=request.POST['last_name']
#         user_email = request.POST['email']
#         user_password=request.POST['password']
#         user = User.objects.create_user(username=user_email,email=user_email,password=user_password,first_name=first_name,last_name=last_name)
#         print(user)
#     return render(request, 'register.html',{})
# CTRL+K CTRL+CS
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Autheticate 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user= authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,"You have successfuly Registerd! welcome")
            return redirect('home')
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'register.html',{'form':form})
    return render(request, 'register.html',{'form':form})

def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record= Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record}) 
    else:
        messages.success(request,"You must be logged in")
        return redirect('home')

def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"Deleted Successfuly")
        return redirect('home')
    else:
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.method =='GET':
        return render(request,'add_record.html',{})
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request,"Record Added..")
                return redirect('home')
            else:
                messages.error(request, "Invalid form..")
                return redirect('home')
    else:
        messages.error(request,"You must login first..")
        return redirect('home')
        #first_name= request.POST['first_name']

def update_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        if request.method == 'GET':
            return render(request, 'update_record.html',{'record':record})
        if request.method =='POST':
            form = AddRecordForm(request.POST or None)
            if form.is_valid():
                form.save()
                record.delete()
                messages.success(request,"Record has been saved")
                return redirect('home')
            else:
                messages.error(request,"Invalid form..")
                return redirect('home')
    else:
        messages.error(request,"You must be logged in first")
        return redirect('home')
