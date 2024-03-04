from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout  
from django.contrib import messages   
from .models import Appuser
from django.shortcuts import get_object_or_404


# Create your views here.
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pass')

        # check the username...
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username!')
            return redirect("/")

        # authenticate the user....
        user = authenticate(request, username=username, password=password)

        # login the user.....
        if user is None:
            messages.error(request, 'Invalid Password!')
            return redirect("/")
        else:
            login(request, user)
            return redirect("/home/")

    return render(request, 'login.html')


def signupPage(request):
    if request.method =="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        picture = request.FILES.get('picture')
        password = request.POST.get('pass')
        cpassword = request.POST.get('pass1')
        if password != cpassword:
            messages.error(request, "Password and Confirm Password not same! ")
            return redirect("/signup/")
        user = User.objects.filter(username = username)
        if user.exists():
            messages.error(request, "Username Already taken!")
            return redirect("/signup/")

        user = User.objects.create_user(username,email,password)
        user.save()
        appuser = Appuser(user = user,picture = picture)
        appuser.save()
        messages.success(request, "Account Created Succcesfully!")
        return redirect("/")
    return render(request,'signup.html')

def index(request):
    app_user = get_object_or_404(Appuser, user=request.user)
    return render(request, 'index.html', {'app_user': app_user})

def addLinks(request):
    return render(request , 'addlink.html')

def handleLogout(request):
    if request.user:
        logout(request)
        return redirect("/")

    return HttpResponse("<h1>Error 404-Page Not Found!!!</h1>")
