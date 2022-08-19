from django.shortcuts import render,redirect
from Ajah.forms import CourseForm, AttendanceForm,GradeForm
from .models import *

# Create your views here.

def course(request):
    
   


    if request.method=='GET':
        form =CourseForm()
                   
    else:
        form=CourseForm(request.POST)
        form.save()
        return redirect('activity')

    context = {'form':form}
            
    return render(request,'ajah/coursework.html',context)




def attendance(request):
    
   


    if request.method=='GET':
        form2 =AttendanceForm()
                   
    else:
        form2=AttendanceForm(request.POST)
        form2.save()
        return redirect('activity')

    context = {'form2':form2}
            
    return render(request,'ajah/attendance.html',context)

def grade(request):
    
   


    if request.method=='GET':
        form3 =GradeForm()
                   
    else:
        form3=GradeForm(request.POST)
        form3.save()
        return redirect('grade')

    context = {'form3':form3}
            
    return render(request,'ajah/grades.html',context)



def activity(request):
    return render(request, 'ajah/activity.html')