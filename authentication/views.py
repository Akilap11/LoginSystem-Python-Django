from django.http import HttpResponse
from django.shortcuts import redirect, render

#import inbuild database
from django.contrib.auth.models import User
#import message
from django.contrib import messages
#import authentication django inbuilt
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request,"authentication/index.html")

def signup(request):
    if request.method=="POST":
        #username=request.POST.get('username')
        username=request.POST['username']
        fname=request.POST['fname']
        email=request.POST['email']
        pw=request.POST['pw']
        cpw=request.POST['cpw']

        myuser=User.objects.create_user(username,email,pw)
        myuser.first_name=fname

        myuser.save()

        messages.success(request,"Account Created Successfully")

        return redirect('signin')

    return render(request,"authentication/signup.html")

def signin(request):

    if request.method=='POST':
        username=request.POST['username']
        pw=request.POST['pw']

#inbuilt django authenticator
        user=authenticate(username=username,password=pw)

        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,"authentication/index.html",{'fname':fname})
        else:
            messages.error(request,"Bad Credentials")
            return redirect('home')


    return render(request,"authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect('home')