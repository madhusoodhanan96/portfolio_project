from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate

def signup(request):
    if request.method == 'POST':
        if request.POST['pass1'] == request.POST['pass2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'accounts/login.html',{'message':'User Exist. Try Login!'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['pass1'])
                auth.login(request,user)
                return redirect('home')
        else:
                return render(request,'accounts/signup.html',{'message':'Password Mismatch'})
    else:
        return render(request,'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['pass'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/login.html',{'message':'User ID or Password is Wrong'})
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
