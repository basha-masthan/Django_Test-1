from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Course,usrData


def register(request):
    course = Course.objects.all()
    return render(request,'register.html',{'course':course})

def home(request):
    itms = Course.objects.all()
    return render(request, 'ind1.html',{'itms':itms})


def usrpage(request):
    if request.method == 'POST':
        usrid = request.POST.get('usrid')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        mail = request.POST.get('gmail')
        mobile = request.POST.get('mobile')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        edu = request.POST.get('edu')
        course_data = request.POST.get('course')
        usr = request.POST.get('usrname')
        pswd = request.POST.get('password')

        en = usrData(usrid=usrid,fname=fname, lname=lname,email=mail,mobile=mobile,gender=gender,address=address,edu=edu,cors=course_data,usr=usr,pswd=pswd)
        en.save()
        return redirect('/login/')
    pass
    return render(request,'ind1.html')

def login(request):
    usrs = usrData.objects.all()
    for user in usrs:
        if user.usr == request.POST.get('username'):
            if user.pswd == request.POST.get('pswd'):
                # return redirect('/usrp/')
                r=Course.objects.get(name=user.cors)
                # return redirect('/usrp/')
                return render(request,'usrp.html',{'user': user,'course': r})
    return render(request,'login.html',{'usrs':usrs,'msg':"Invalid username or password"})


@login_required
def usrp(request):
    return render(request,'usrp.html')


def usredit(request):
    users = usrData.objects.all()


    # if request.method == 'POST':
        # user = request.POST.get('user')
        # fname = request.POST.get('fname')
        # lname = request.POST.get('lname')
        # mail = request.POST.get('gmail')
        # mobile = request.POST.get('mobile')
        # gender = request.POST.get('gender')
        # address = request.POST.get('address')
        # edu = request.POST.get('edu')
        # pswd = request.POST.get('password')

        # try:
        #     usr = usrData.objects.get(email=mail)
        # except usrData.DoesNotExist:
        #     return redirect('/usredit/')
        # usr.fname = fname
        # usr.lname = lname
        # usr.email = mail
        # usr.mobile = mobile
        # usr.gender = gender
        # usr.address = address
        # usr.edu = edu
        # usr.pswd = pswd
        # usr.update()
        # return redirect('/usrp/')


    return render(request,'usredit.html')





def logout(requset):
    return redirect('/')