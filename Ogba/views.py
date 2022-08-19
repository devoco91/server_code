from django.shortcuts import render, redirect
from Ogba.forms import OCourseForm, OAttendanceForm, OGradeForm
from .models import *

# Create your views here.

def ocourse(request):
    
   


    if request.method=='GET':
        form7 =OCourseForm()
                   
    else:
        form7=OCourseForm(request.POST)
        form7.save()
        return redirect('oactivity')

    context = {'form7':form7}
            
    return render(request,'ogba/ocoursework.html',context)

def oattendance(request):
    
   


    if request.method=='GET':
        form8 =OAttendanceForm()
                   
    else:
        form8=OAttendanceForm(request.POST)
        form8.save()
        return redirect('oactivity')

    context = {'form8':form8}
            
    return render(request,'ogba/oattendance.html',context)

def ograde(request):
    
   


    if request.method=='GET':
        form9 =OGradeForm()
                   
    else:
        form9=OGradeForm(request.POST)
        form9.save()
        return redirect('ograde')

    context = {'form9':form9}
            
    return render(request,'ogba/ogrades.html',context)



def oactivity(request):
    return render(request, 'ogba/oactivity.html')