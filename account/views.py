from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import price
# Create your views here.
def register(request):
   if request.method == 'POST':
      username=request.POST['name']
      number=request.POST['number']
      password1=request.POST['password1']
      password2=request.POST['password2']
      email=request.POST['email']
      if username :
         if number:
            if password1:
               if password2:
                  if email:             
                        if User.objects.filter(username=username).exists():
                              messages.error(request,"Username exist")
                              return render(request,'register.html')
                           
                        elif User.objects.filter(email=email).exists():
                              messages.error(request,"Email exist")
                              return render(request,'register.html')
                        elif password1!=password2:
                              messages.error(request,"Passwrd not match ")
                              return render(request,'register.html')
                        else:
                              user=User.objects.create_user(username=username,password=password1,email=email)
                              user.save();
                              messages.success(request,'User created')
                              return redirect('login')
                  else:
                        messages.error(request,"Enter email ")
                        return render(request,'register.html')
               else:
                     messages.error(request,"Enter Password ")
                     return render(request,'register.html')
            else:
                  messages.error(request,"Enter Password ")
                  return render(request,'register.html')
         else:
             messages.error(request,'Enter number')
             return redirect(request,'register.html')
      else:
         messages.error(request,'Enter Name')
         return redirect(request,'register.html')
          
          
                         
   else:
      return render(request,'register.html')
     
def login(request):
   if request.method == 'POST':
      username=request.POST['name']
      password=request.POST['password']
      user=auth.authenticate(username=username,password=password)

      if user is not None:
         auth.login(request,user)
         return redirect('/')
      else:
         messages.error(request,"Invalid credential")
         return redirect('login')
   else:
      return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

def cart(request):
      return render(request,'cart.html')
    