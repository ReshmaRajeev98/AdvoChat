from django.shortcuts import render, redirect
from .models import *
from UserApp.models import LawyerDB, UserDB, BookDB, MsgDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

def Admin(request):
    Lawyer = LawyerDB.objects.filter(status_l='Accepted').count()
    User = UserDB.objects.filter(status_r='Accepted').count()
    Cases = BookDB.objects.filter(status='Accepted').count()
    msgs = MsgDB.objects.all().count()
    return render(request, "Admin.html", {'data':Lawyer, 'user':User, 'Cases':Cases, 'msgs':msgs})

def AddLaw(request):
    return render(request, "AddLaw.html")

def getLaw(request):
    if request.method=="POST":
        id = request.POST.get('id')
        type = request.POST.get('type')
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        data = LawsDB(id=id, type=type, name=name, desc=desc)
        data.save()
        return redirect(ViewLaw)

def ViewLaw(request):
    data = LawsDB.objects.all()
    return render(request,'ViewLaw.html',{'data':data})

def delete(request,id):
    LawsDB.objects.filter(id=id).delete()
    return redirect('ViewLaw')

def edit(request,eid):
    data = LawsDB.objects.filter(id=eid)
    return render(request,"UpdateLaw.html",{'data':data})

def UpdateLaw(request,id):
    if request.method == "POST":
        id = request.POST.get('id')
        type = request.POST.get('type')
        name = request.POST.get('name')
        desc = request.POST.get('desc')
    LawsDB.objects.filter(id=id).update(id=id, type=type, name=name, desc=desc)
    return redirect('ViewLaw')

def ViewLawyerReq(request):
    data = LawyerDB.objects.filter(status_l='null')
    return render(request,'ViewLawyerReq.html',{'data':data})

def AcceptLawyerReq(request,LRAid):
    LawyerDB.objects.filter(id=LRAid).update(status_l='Accepted')
    return redirect(ViewLawyerReq)

def RejectLawyerReq(request,LRDid):
    if request.method=="POST":
        reason = request.POST.get('reason')
    else:
        data = LawyerDB.objects.filter(id=LRDid)
        return render(request, "RejectLawyerReq.html", {'data':data})
    LawyerDB.objects.filter(id=LRDid).update(status_l='Rejected',reason_l=reason)
    return redirect(ViewLawyerReq)

def ViewLawyers(request):
    data = LawyerDB.objects.filter(status_l='Accepted')
    return render(request,'ViewLawyers.html',{'data':data})

def ViewUserReq(request):
    data = UserDB.objects.filter(status_r='null')
    return render(request,'ViewUserReq.html',{'data':data})

def AcceptUserReq(request,UAid):
    UserDB.objects.filter(id=UAid).update(status_r='Accepted')
    return redirect(ViewUserReq)

def RejectUserReq(request,UDid):
    if request.method=="POST":
        reason = request.POST.get('reason')
    else:
        data = UserDB.objects.filter(id=UDid)
        return render(request, "RejectUserReq.html", {'data':data})
    UserDB.objects.filter(id=UDid).update(status_r='Rejected',reason_r=reason)
    return redirect(ViewUserReq)

def ViewCases(request):
    data = BookDB.objects.all()
    return render(request,'ViewCases.html',{'data':data})

def ViewUsers(request):
    data = UserDB.objects.filter(status_r='Accepted')
    return render(request,'ViewUsers.html',{'data':data})