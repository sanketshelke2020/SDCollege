from email import message
from urllib import response
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import UserExtended,Course
from django.urls import reverse
from django.core.mail import EmailMessage


# Create your views here.
def register(request):
    course = Course.objects.all()
    if request.method  == "POST":
        email = request.POST["email"]
        username = email.split("@")[0]
        password = request.POST["password"]
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        course_name = request.POST["course"]

        allUsers = User.objects.all()

        for user in allUsers:
            if username == user.username:
                return render(request, "dashboard/register.html", context={
                    "message" : "User Already Exists !"
                })

        user = User.objects.create_user(username,email,password)
        
        mycourse = Course.objects.get(courseAbbr = course_name)

        # UserExtended        

        userExt = UserExtended()
        userExt.user = user
        userExt.course = mycourse
        userExt.save()

        user.first_name = first_name
        user.last_name = last_name
        user.save()

        return render(request,"dashboard/login.html", context={
            "message": "Registration Successful"
        })

    # getting every studnet from course
        # for uuser in mycourse.courseusers.all():

        #     print(uuser.user.username)

    return render(request,"dashboard/register.html",context= {
        "courses" : course
    })


def loginView(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Check if username is email or username
        if "@" in username:
            username = username.split("@")[0]

        user = authenticate(request, username = username, password = password)

        if user is not None :
            login(request,user)
            return HttpResponseRedirect("dashboard")

        else :
            return render(request, "dashboard/login.html", context={
                "message" : "Invalid Email or Password"
            })


    return render(request,"dashboard/login.html")

def dashboard(request):
    """Dashboard View Function """
    if request.user.is_authenticated:
        print("hello", request.user.username)
        return render(request, "dashboard/dashboard.html")

def logoutView(request):
    """Logout View Function """
    logout(request)
    return render(request,"dashboard/login.html", context={
            "message": "Logout Successful"
        })