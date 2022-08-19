from django.shortcuts import render, redirect
from Berger.forms import BCourseForm, BAttendanceForm, BGradeForm
from .models import *

# Create your views here.

def bcourse(request):
    
   


    if request.method=='GET':
        form4 =BCourseForm()
                   
    else:
        form4=BCourseForm(request.POST)
        form4.save()
        return redirect('bactivity')

    context = {'form4':form4}
            
    return render(request,'berger/bcoursework.html',context)

def battendance(request):
    
   


    if request.method=='GET':
        form5 =BAttendanceForm()
                   
    else:
        form5=BAttendanceForm(request.POST)
        form5.save()
        return redirect('bactivity')

    context = {'form5':form5}
            
    return render(request,'berger/battendance.html',context)

def bgrade(request):
    
   


    if request.method=='GET':
        form6 =BGradeForm()
                   
    else:
        form6=BGradeForm(request.POST)
        form6.save()
        return redirect('bgrade')

    context = {'form6':form6}
            
    return render(request,'berger/bgrades.html',context)



def bactivity(request):
    return render(request, 'berger/bactivity.html')