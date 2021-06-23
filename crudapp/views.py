
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .forms import studentRegistration
from .models import User
from django.contrib import messages

# Create your views here.
def addshow(request):
    if request.method =='POST':
        fm = studentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            cn = fm.cleaned_data['contact']
            ps = fm.cleaned_data['password']
            rg = User(name=nm,email=em,contact=cn,password=ps)
            rg.save()
            messages.success(request,'you have data submitted!')
            fm = studentRegistration()
    else:
        fm = studentRegistration()
    stud = User.objects.all()
    return render(request,'crud/addshow.html',{'form':fm,'stu':stud})

# this function update/edit
def update_data(request,id):
    if request.method=='POST':
        pi = User.objects.get(pk=id)
        fm = studentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
    fm = studentRegistration(instance=pi)
    return render(request,'crud/update.html',{'form':fm})





# This function will delete
def delete_data(request,id):
    if request.method=='POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

