from django.shortcuts import render
from .models import userDetail
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    if request.method=='POST':
        em=request.POST.get('email')
        pass1=request.POST.get('pass')
        obj=userDetail.objects.all()
        for row in obj:
            if row.email== em:
                if row.password == pass1:
                    messages.success(request,"You are logged in succesfully!") 
                    return render(request,'home.html')
                else:
                    messages.success(request,"You entered a wrong password!") 
                    return render(request,'home.html')
        messages.warning(request,"You entered a wrong email!") 
    return render(request,'home.html')
    

def signup(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if pass1==pass2:
            usdet=userDetail(name=name,email=email,password=pass1)
            usdet.save()
            messages.success(request,"Your form has been submitted")
        else:
            messages.warning(request,"Your have entered a wrong password")
    return render(request,'home.html')
    