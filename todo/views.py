from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import TODOO
from django.contrib.auth import authenticate,login,logout

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print( name,  email, password )

        my_user = User.objects.create_user(username=name, email=email, password=password)
        my_user.save()
        return redirect('/login')

    return render(request, 'signup.html')

def loginn(request):
     if request.method == 'POST':
        name = request.POST.get('username')
        Password = request.POST.get('password')
        userr=authenticate(request,username=name, password=Password)
        if userr is not None:
            login(request,userr)
            return redirect('/todopage')
        else:
            return redirect('/login')

    
     return render(request, 'login.html')
