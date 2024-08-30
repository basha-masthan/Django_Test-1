from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Course,usrData,cart
import random
from django.contrib.auth import logout

def register(request):
    course = Course.objects.all()
    return render(request,'register.html',{'course':course})

def home(request):
    itms = Course.objects.all()
    return render(request, 'ind1.html',{'itms':itms})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def usrpage(request):
    usercourse = cart.objects.all()
    dbcourse = Course.objects.all()
    if request.method == 'POST':
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
        en = usrData(fname=fname, lname=lname,email=mail,mobile=mobile,gender=gender,address=address,edu=edu,cors=course_data,usr=usr,pswd=pswd)
        en.save()
        
        return redirect('/login/')
    pass
    return render(request,'ind1.html')

def login(request):
    usrs = usrData.objects.all()
    try:
        usr = usrData.objects.get(usr=request.POST.get('username'),pswd=request.POST.get('pswd'))
        # r=Course.objects.get(name=usr.cors)
        # d = cart(usrid=usr.id,course=r.name,price=r.price)
        # try:
        #     t=cart.objects.get(course=usr.cors)
        # except Exception as e:
        #     d.save()
        # _carts = cart.objects.all()
        request.session['usr']=usr.usr
        return redirect('/usrp')

        # return render(request,'usrp.html',{'user': usr,'course': r,'cart':carts})
    except Exception as e:
        pass    
    return render(request,'login.html',{'usrs':usrs,'msg':"Invalid username or password"})



def usrp(request):
    user = request.session['usr']
    usrs = usrData.objects.get(usr=user)
    r=Course.objects.get(name=usrs.cors)
    return render(request,'usrp.html',{'user':usrs,'course': r})


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



def usr_cart(request):
    # cart = cart.objects.get(usrid=request.POST.get('usrid'))
    itms = Course.objects.all()
    if request.method == 'POST':
        usrid = request.POST.get('user_id')
        usr = usrData.objects.get(email=usrid)
        return render(request,'usrcart.html',{'user':usr,'itms': itms,'cart':cart})

    return render(request,'usrp.html')


def usrcart_add(request):
    itms = Course.objects.all()
    usrs = usrData.objects.all()
    carts = cart.objects.all()
    if request.method == 'POST':
        usrid = request.POST.get('usrid')
        course = request.POST.get('cname')
        r= Course.objects.get(name=course)
        k=usrData.objects.get(id=usrid)
        d= cart(usrid=k.id,course=course)
        d.save()
        return HttpResponse("Course Added")
    return redirect('/cart/')
    
def logout_1(request):
    # logout(request)
    return redirect('/login/') 

def payment(request):
    user = request.session['usr']
    usrs = usrData.objects.get(usr=user)
    r=Course.objects.get(name=usrs.cors)
    rr = r.name
    return render(request,'payment.html',{'course':rr})


def usrgd(request):
    user = request.session['usr']
    usrs = usrData.objects.get(usr=user)
    r=Course.objects.get(name=usrs.cors)
    rr = r.name
    return render(request,'usrgd.html',{'user':usrs,'course': rr})

def delcard(request):
    carts = cart.objects.get(course=request.POST.get('cname'))

    carts.delete()
    return HttpResponse("Card Deleted")

def adminpage(request):
    users = usrData.objects.all()
    courses = Course.objects.all()
    return render(request,'admin/dashboard.html',{'users': users,'course': courses,'k':0})

def mb_course(request):
    users = usrData.objects.all()
    courses = Course.objects.all()
    return render(request,'admin/mb_course.html',{'users': users,'course': courses})

