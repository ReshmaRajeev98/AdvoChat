import email
from email import message
import re
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from AdminApp.models import LawsDB 

# Create your views here.

def User(request):
    data = LawsDB.objects.all()
    return render(request, "User.html", {'data':data})

def UserReg(request):
    return render(request, 'UserReg.html')

def getDataUser(request):
    if request.method=="POST":
        name_r = request.POST.get('uname')
        phone_r = request.POST.get('phn')
        email_r = request.POST.get('email')
        pwd_r = request.POST.get('pwd')
        data = UserDB(name_r=name_r, phone_r=phone_r, email_r=email_r, pwd_r=pwd_r)
        data.save()
        return redirect(User)

def Login(request):
    if request.method=="POST":
        email_r = request.POST.get('uname')
        pwd_r = request.POST.get('pwd')
        print(email_r, pwd_r)
        if UserDB.objects.filter(email_r=email_r,pwd_r=pwd_r):
            data = UserDB.objects.filter(email_r=email_r,pwd_r=pwd_r).values('name_r','id').first()
            request.session['username'] = email_r
            request.session['password'] = pwd_r
            request.session['name'] = data['name_r']
            request.session['id'] = data['id']
            messages.success(request, "Login Successful")
            return redirect(User)
        
        elif LawyerDB.objects.filter(email_l=email_r, pwd_l=pwd_r):
            data = LawyerDB.objects.filter(email_l=email_r, pwd_l=pwd_r).values('name_l','id').first()
            request.session['uname'] = email_r
            request.session['pwd'] = pwd_r
            request.session['name_l'] = data['name_l']
            request.session['id_l'] = data['id']
            messages.success(request, "Login Successful")
            return redirect(User)
        else:
            messages.error(request, "Unknown User")
            return redirect(UserReg)

def LawyerReg(request):
    data = LawsDB.objects.all()
    return render(request, 'LawyerReg.html', {'data':data})

def getDataLawyer(request):
    if request.method=="POST":
        name_l = request.POST.get('uname')
        phone_l = request.POST.get('phn')
        enroll_l = request.POST.get('enr')
        law = request.POST.get('law')
        email_l = request.POST.get('email')
        pwd_l = request.POST.get('pwd')
        image = request.FILES['image']
        data = LawyerDB(name_l=name_l, phone_l=phone_l, enroll_l=enroll_l,law=law, email_l=email_l, pwd_l=pwd_l,image=image)
        data.save()
        return redirect(User)

def user_logout(request):
    del request.session['username']
    del request.session['password'] 
    del request.session['name']
    del request.session['id']
    return redirect(User)

def Laywer_logout(request):
    del request.session['uname']
    del request.session['pwd'] 
    del request.session['name_l']
    del request.session['id_l']
    return redirect(User)

def FindLawyer(request,name):
    data = LawyerDB.objects.filter(law=name)
    print(data)
    return render(request, 'FindLawyer.html', {'data':data})

def BookConsult(request):
    return render(request, "BookConsult.html")

def getDataConsult(request):
    if request.method=="POST":
        userid = request.session.get('id')
        subject = request.POST.get('subject')
        desc = request.POST.get('desc')
        data = BookDB(subject=subject, desc=desc, userid=UserDB.objects.get(id=userid))
        data.save()
        return redirect(User)

def Find(request):
    data = LawsDB.objects.all()
    return render(request, "Find.html", {'data':data})

def ViewReq(request):
    data = BookDB.objects.filter(status='null')
    return render(request, "ViewReq.html", {'data':data})

def accept(request,eid):
    if request.method=="POST":
        room = request.POST.get('room')
    else:
        data = BookDB.objects.filter(id=eid)
        return render(request, "accept.html", {'data':data})
    BookDB.objects.filter(id=eid).update(status='Accepted',room=room)
    return redirect(ViewReq)

def decline(request,id):
    if request.method=="POST":
        reason = request.POST.get('reason')
    else:
        data = BookDB.objects.filter(id=id)
        return render(request, "decline.html", {'data':data})
    BookDB.objects.filter(id=id).update(status='Rejected',reason=reason)
    return redirect(ViewReq)

def ViewReqUser(request):
    userid = request.session.get('id')
    data = BookDB.objects.filter(userid=userid)
    return render(request, "ViewReqUser.html", {'data':data})

def resubmit(request,uid):
    if request.method=="POST":
        userid = request.session.get('id')
        subject = request.POST.get('subject')   
        desc = request.POST.get('desc')
    else:
        data = BookDB.objects.filter(id=uid)
        return render(request, "resubmit.html", {'data':data})
    BookDB.objects.filter(id=uid).update(subject=subject, desc=desc, status='null',  reason='null', userid=UserDB.objects.get(id=userid))
    return redirect(ViewReqUser)

def ContactUs(request):
    return render(request, "ContactUs.html")

def getDataMsg(request):
    if request.method=="POST":
        name_m = request.POST.get('name')
        email_m = request.POST.get('email')
        phone_m = request.POST.get('phone')
        reason_m = request.POST.get('reason')
        message_m = request.POST.get('message')
        data = MsgDB(name_m=name_m, email_m=email_m, phone_m=phone_m, reason_m= reason_m, message_m= message_m)
        data.save()
        return redirect(ContactUs)