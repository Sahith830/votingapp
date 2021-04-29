from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from .models import Candidates,UserVote
import math,shutil,os
# Create your views here.
def index(request):
    return render(request,'index.html')


def registration(request):
    if(request.method=='GET'):
        return render(request,'register.html')
    uname = request.POST["username"]
    pwd = request.POST["pwd"]
    name = request.POST['name']
    email = request.POST['email']
    if(User.objects.filter(username=uname).exists()):
        messages.error(request,"Username Already Exits")
        return redirect('register')
    user = User.objects.create_user(username = uname,password=pwd,email = email,first_name = name)
    userVote = UserVote()
    userVote.user = user
    userVote.save()
    messages.success(request,'User Created Successfully , Please Login to Continue')
    print("USer Created")
    return redirect('login')

def home(request):
    candidates = Candidates.objects.all()
    u = UserVote.objects.get(user=request.user)
    if(request.method=='GET'):
        return render(request,'homepage.html',{'candidates':candidates,'votedto':u.votedto,'isvoted': u.isVoted })
    vote = ""
    for i in  candidates:
        if(i.name in request.POST.keys()):
            vote = i.name
            break
    u.isVoted = True
    u.votedto = vote
    u.save()
    return redirect('home')
def signout(request):
    logout(request)
    return redirect('/')

def adminreg(request):
    if(request.method=="POST"):
        uname = request.POST["username"]
        pwd = request.POST["pwd"]
        name = request.POST['name']
        email = request.POST['email']
        user = User.objects.create_user(username = uname,password=pwd,email = email,first_name = name,is_superuser=True,is_staff= True)
        user.save()
        print("Super User Created")
        return redirect('login')
    return render(request,'adminReg.html')

def addcandidate(request):
    if(request.method=="GET"):
        return render(request,'addCandidate.html')
    candidate  = Candidates()
    candidate.name = request.POST["name"]
    candidate.party = request.POST["party"]
    candidate.symbol = request.POST['symbol']
    myfile = request.FILES['imagefile']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    candidate.img = myfile.name
    candidate.save()
    print("Created Candidate Successfully ")
    return redirect("adminHome")


def delCandidate(request):
    candidates = Candidates.objects.all()
    if(request.method=='GET'):
        return render(request,'deleteCandidate.html',{'candidates':candidates})
    print(request.POST)
    for i in candidates:
        if(i.name in request.POST.keys()):
            c = Candidates.objects.get(name=i.name,party=i.party,symbol=i.symbol)
            c.delete()
            v = UserVote.objects.filter(isVoted=True,votedto=i.name)
            v.delete()
    return redirect('adminHome')

def adminHome(request):
    if(request.method=="POST"):
        if('del' in request.POST.keys()):
            return redirect("deletecandidate",)
        return redirect("addcandidate")
    result = []
    candidates = Candidates.objects.all()
    totalvotes = len(UserVote.objects.filter(isVoted=True))
    for i in candidates:
        t = UserVote.objects.filter(isVoted=True,votedto=i.name)
        result.append((i.name,round((len(t)/totalvotes)*100,2),len(t)))
    candidates = Candidates.objects.all()
    return render(request,'adminHome.html',{'result':result,'candidates':candidates,'total':totalvotes})

def forgotpwd(request):
    if(request.method=='GET'):
        return render(request,'forgotpwd.html')
    uname = request.POST["username"]
    name = request.POST['name']
    email = request.POST['email']
    pwd = request.POST["pwd"]
    user = User.objects.get(username=uname,email=email,first_name=name)
    print(user)
    if(user is not None):
        user.set_password(pwd)
        user.save()
        print("User password changed Successfully")
        messages.success(request,"Password Set Successfully")
        return redirect('login')
    messages.error(request,"User Not found , please Try Again")
    return redirect('forgotpassword')


def profile(request):
    if(request.method=='GET'):
        print(request.body,request.content_type,request.content_params,request.COOKIES)
        return render(request,'profile.html',{'userdata':request.user})
    oldpwd = request.POST["oldpassword"]
    newpwd = request.POST["newpassword"]
    if(check_password(oldpwd,request.user.password)):
        print("Password Matches")
        user = request.user
        user.set_password(newpwd)
        user.save()
        print("Successfully updated Password")
        return redirect('login')
    messages.error = "old Password didn't matched with your password , Please try again"
    return redirect('profile')
def loginUser(request):
    if(request.method=='GET'):
        return render(request,'login.html')
    uname = request.POST["username"]
    pwd = request.POST["pwd"]
    user = authenticate(request=request,username=uname,password=pwd)
    if(user is None):
        return redirect('login')
    login(request,user)
    if(user.is_superuser==True):
        return redirect('adminHome')
    return redirect('home')