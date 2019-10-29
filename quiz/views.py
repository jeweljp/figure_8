from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponse,HttpResponseRedirect
from . models import *
from datetime import datetime


@csrf_protect
#login_user function is to handle the logging in of user
def login_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home')
    if request.method == 'GET':
        return render(request,'login.html',{})
    if request.method ==  'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/home')
            else :
                raise Exception
        except Exception as e:
            return render(request,'login.html',{'obj':'Invalid user name or password'})

def home(request):
    if request.user.is_authenticated:
        try:
            user = fig.objects.get(uname = request.user.username)
            lev = user.level
            if lev == 12:
                return render(request,'won.html',{'username':str(request.user.username)})
            return render(request,'level'+str(lev)+'.html',{'username':str(request.user.username)})
        except Exception as e:
            user = fig(uname = request.user.username)
            user.save()
            return render(request,'level0.html',{'username':str(request.user.username)})
    else:
        return render(request,'login.html',{'obj':'Please login first'})

def ans_check(request):
    if request.user.is_authenticated:
        ans = request.POST.get('Key').lower().replace(' ','')
        user = fig.objects.get(uname = request.user.username)
        obj = level.objects.get(level = user.level)
        ansc = obj.ans.lower().replace(' ','')
        if ans == ansc:
            print ("Inside")
            if user.timeval == None:
                user.timeval=''
            user.timeval = user.timeval + ',' + str(datetime.now())
            user.level+=1
            user.save()
            if user.level == 4:
                return HttpResponseRedirect('/level2')
            if user.level == 9:
                return HttpResponseRedirect('/home.-_--._.')        
            elif user.level == 10:
                return HttpResponseRedirect('/home/tempus')
            else:
                return HttpResponseRedirect('/home')
        else:
            return HttpResponseRedirect('/home')
    else:
        return render(request,'login.html',{'obj':'Please login first'})   

def level3(request):
    if request.user.is_authenticated:
        user = fig.objects.get(uname = request.user.username)
        if user.level == 4:
            user.level+=1
            user.save()
            return HttpResponseRedirect('/home')
    else:
        return render(request,'login.html',{'obj':'Please login first'})

def logout_user(request):
    logout(request)
    return render(request,'login.html',{'obj':'Logged out successfully'})
