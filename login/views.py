from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout  
from django.contrib import messages   
from .models import Appuser
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, update_session_auth_hash


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

def addLinks(request,id):
    user = User.objects.get(username = id)
    app_user = get_object_or_404(Appuser, user=request.user)
    links = Appuser.objects.get(user = user)
    if request.method == "POST":
        facebook = request.POST.get("facebook")
        twitter = request.POST.get("twitter")
        instagram = request.POST.get("instagram")
        youtube = request.POST.get("youtube")

        appuser, created = Appuser.objects.get_or_create(user=user)

        appuser.facebook = facebook
        appuser.twitter = twitter
        appuser.instagram = instagram
        appuser.youtube = youtube
    
    # Save the changes to the database
        appuser.save()
        messages.success(request, "Links Updated Successfully!")
    return render(request , 'addlink.html', {'app_user': app_user,'links':links})

def handleLogout(request):
    if request.user:
        logout(request)
        return redirect("/")

    return HttpResponse("<h1>Error 404-Page Not Found!!!</h1>")


@login_required
def change_password(request):
    app_user = get_object_or_404(Appuser, user=request.user)
    if request.method == "POST":
        opass = request.POST.get('opass')
        npass = request.POST.get('npass')
        cpass = request.POST.get('cpass')
        # Authenticate the user
        user = authenticate(username=request.user.username, password=opass)
        if user is not None:
            # Check if new password and confirm password match
            if npass == cpass:
                # Change the user's password
                user.set_password(npass)
                user.save()

                # Update session authentication hash to prevent logout
                update_session_auth_hash(request, user)

                messages.success(request, 'Password changed successfully.')
                return redirect('/changePassword/')  # Redirect to success page or any other page
            else:
                messages.error(request, 'password do not match.')
        else:
            messages.error(request, 'Invalid old password.')
    return render(request, 'changepass.html',{'appuser':app_user})