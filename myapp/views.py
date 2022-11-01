
from email import message
from pyexpat.errors import messages
import re 
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, logout
from django.urls import is_valid_path
from setuptools import sic
from .forms import SignupForm,PatientForm
from .models import Signup,Patient

# Create your views here.

def index(request):
    user=request.session.get('user')
    return render(request,'index.html',{'user':user})

def signup(request):
    if request.method=='POST':
        newform=SignupForm(request.POST)
        if newform.is_valid():
            newform.save()
            return redirect('login')
        else:
            print(newform.errors)
    else:
        newform=SignupForm()               
    return render(request,'signup.html',{'newform':newform})   

def login(request):
    if  request.method == 'POST':
        email=request.POST['email']
        pas=request.POST['password']
        login_check=Signup.objects.filter(email=email,password=pas)
        if login_check:
            print('login success')
            request.session['user']=email
            return redirect('index')
        else:
          
            print("Error")  
            return redirect('login')  
    else:
        print('Error')        
    return render(request,'login.html') 

def userlogout(request):
    
    logout(request)
    return redirect('login')

def patient(request):
    user=request.session.get('user')
    if request.method == 'POST':
        form=PatientForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)  
    else:
        print('done')          
    user=request.session.get('user')
    return render(request,'patient.html',{'user':user})   

def userprofile(request):
    user=request.session.get('user')
    userid=Signup.objects.get(email=user)
    if request.method=='POST':
        signupfrm=SignupForm(request.POST)
        if signupfrm.is_valid():
            signupfrm=SignupForm(request.POST,instance=userid)
            signupfrm.save()
            print('updated')
            return redirect('index')
        else:
            print(signupfrm.errors)

    else:
        print('Error')                
    return render(request,'userprofile.html',{'user':user, 'userid':Signup.objects.get(email=user)})
       
  
def updateuserprofile(request):
    user=request.session.get('user')
    userid=Signup.objects.get(email=user)
    if request.method=='POST':
        signupfrm=SignupForm(request.POST)
        if signupfrm.is_valid():
            signupfrm=SignupForm(request.POST,instance=userid)
            signupfrm.save()
            print('updated')
            return redirect('index')
        else:
            print(signupfrm.errors)

    else:
        print('Error')                
    return render(request,'updateuserprofile.html',{'user':user, 'userid':Signup.objects.get(email=user)})


def appointment(request):
    user=request.session.get('user')
    userid=Patient.objects.get(patientemail=user)
    if request.method=='POST':
        patientfrm=PatientForm(request.POST)
        if patientfrm.is_valid():
            patientfrm=PatientForm(request.POST,instance=userid)
            patientfrm.save()
            print('updated')
            return redirect('index')
        else:
            print(patientfrm.errors)

    else:
        print('Error')                
    return render(request,'appointment.html',{'user':user, 'userid':Patient.objects.get(patientemail=user)})   
    