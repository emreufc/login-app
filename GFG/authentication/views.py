from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def register_request(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "authentication/register.html",{"error:":"Username already exist!"})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request,"authentication/register.html",{"error":"This e-mail address is already in use!"})
                else:
                    myuser = User.objects.create_user(username=username,email=email,first_name=fname,last_name=lname,password=password)
                    myuser.save()
                    return redirect("login")
        else:
            return render(request, "authentication/register.html",{"error":"Passwords do not match!"})

    return render(request, "authentication/register.html")

def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user =  authenticate(request, username=username, password= password)


        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            
            return render(request, "authentication/login.html",{
                "error": "Bad credentials!"
            })
        
    return render(request, "authentication/login.html")
    

def logout_request(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('login')