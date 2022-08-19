
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required


def registrationPage(request):
    if request.user.is_authenticated:
        return redirect('center')


    else:


        
        form=CreateUserForm()
        if request.method=='POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,'Account was created for ' + user)
                return redirect('login')

        
                

        context = {'form':form}
        return render(request, 'register.html', 
        context)


def loginPage(request):


    if request.user.is_authenticated:
        return redirect('center')

    else:
            
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)


            if user is not None:
                login(request, user)
                return redirect('center')

            else:
                messages.info(request, 'Username OR Password is incorrect')

        return render(request,'login.html')



def logoutUser(request):
    logout(request)
    return redirect('login')


# @login_required(login_url='login')
def home(request):
    
    return render(request,'index.html')

@login_required(login_url='login')
def center(request):
    
    return render(request,'center.html')


