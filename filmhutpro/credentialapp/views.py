from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MovieForm

# Create your views here.
#Login

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('filmapp:index')
        else:
            messages.info(request, "invalid credentials")
            return  redirect('credentialapp:login')


    return render(request,'login.html')

#Register

def register(request):
    if request.method=="POST":
        username=request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['confirmpassword']
        if password==cpassword:
            if User.objects.filter(username=username):
                messages.info(request,"username taken")
                return redirect('credentialapp:register')
            elif User.objects.filter(email=email):
                messages.info(request,"email taken")
                return redirect('credentialapp:register')

            else:
                user=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)
                user.save();
                print("user created")
                return redirect('credentialapp:login')
        else:
            messages.info(request, "password not matching")
            return redirect('credentialapp:register')

    return render(request,'register.html')

#Logout

def logout(request):
    auth.logout(request)
    return redirect('/')

#Add movie

@login_required
def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = MovieForm(user=request.user)
    return render(request, "addmovie.html", {'form': form})
