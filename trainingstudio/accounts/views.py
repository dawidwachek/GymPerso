from django.shortcuts import render, redirect
from .models import UserProxy, UserManager, User
from django.contrib.auth import authenticate, login as logfun, logout

def btn_logout(request):
    request.logout(request)
    return redirect('/accounts/register',{})

def accounts(request):
    return redirect('/accounts/login',{})

def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        date_birthday = request.POST.get("date")
        phone_number = request.POST.get("phone")

        #this not working
        #UserManager.create_user(email =email,password=password)
        User.objects.create_user(email=email, password=password)
        UserProxy(email = email, first_name = "", date_birthday = date_birthday ,phone_number = phone_number).save()
        #UserManager.create_user(email=email, password=password)
        #User(email=email, password=password).save()
        
        return redirect('/accounts/register', {})


        #this working
        #UserProxy(email = email, first_name = "", phone_number = 123456700).save()
        

        #upadate data
        #obj = UserProxy.objects.filter(email = email).update(phone_number = 123456700)
        
    if request.user.is_authenticated:
        return redirect('/accounts/profile')
    else: 
        return render(request, 'register.html',{})

    

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request,email=email, password=password)
        print('request: ', request)
        if user is None:
            return redirect('/accounts/login', {})
        #print('email: ', email)
        logfun(request, user)

        return redirect('/accounts/profile', {})
        
    
    #print('user: ', user)
    #if user is None:
      #  pass
        #return render(request, 'login.html',{})
    #else:
     #   pass
        #return render(request, 'profile.html',{})

    #login_test = UserProxy(email= 'dawidwwwww@gmail.com')
    #login_test.save()
    return render(request, 'login.html',{})

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html',{})
    else: 
        return redirect('/accounts/login')