from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import TODOO

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print( name,  email, password )

        my_user = User.objects.create_user(name,email,password)
        my_user.save()
        return redirect('/login')

    return render(request, 'signup.html')

def login(request):
    return render(request, 'signup.html')
