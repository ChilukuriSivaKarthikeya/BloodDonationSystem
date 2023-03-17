from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Donors
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import math,random
obj=""
OTP=""

def home(request):
    return render(request,"home.html")
def login(request):
    if request.method=="POST":
      userid=request.POST["userid"]
      password=request.POST["password"]
      user=Donors.objects.get(email=userid)
      if user.password==password:
            global obj
            obj=user
            return redirect("user")
      else:
         messages.error(request,'Wrong Email or Password')
         return render(request,"login.html")
    else:
       return render(request,"login.html")
def user(request):
    global obj
    return render(request,"userpage.html",{"object":obj})
def profile(request):
    global obj
    return render(request,"profile.html",{"object":obj})
def logout(request):
    return render(request,"home.html")
def search(request):
    if request.method=="POST":
       ele=request.POST["element"]
       group=request.POST["bloodgroup"]
       if group=="all":
         content=Donors.objects.all().order_by('name')
       else:
         content=Donors.objects.filter(bloodgroup=group).order_by('name')
       x=[]
       for i in content:
           print(i.village.lower())
           if ((i.village).replace(" ","").lower()==ele.lower() or str(i.pincode)==ele) and i.status=="True":
               x.append(i)   
       if x==[]:
         messages.info(request,"No result found!")
         return render(request,"search.html",{"search":ele})
       else:
          return render(request,"search.html",{"contents":x,"search":ele})
    else:
       return render(request,"search.html")

def usersearch(request):
    global obj
    if request.method=="POST":
      ele=request.POST["element"]
      group=request.POST["bloodgroup"]
      if group=="all":
         content=Donors.objects.all().order_by('name')
      else:
         content=Donors.objects.filter(bloodgroup=group).order_by('name')
      x=[]
      for i in content:
           if ((i.village).replace(" ","").lower()==ele.lower() or str(i.pincode)==ele) and i.status=="True":
               x.append(i) 
      if x==[]:
        messages.info(request,"No result found!")
        return render(request,"userpagesearch.html",{"search":ele,"object":obj})
      else:
        return render(request,"userpagesearch.html",{"contents":x,"search":ele,"object":obj})
    else:
       return render(request,"userpagesearch.html",{"object":obj})

def register(request):
    if request.method=="POST":
       name=request.POST["name"]
       email=request.POST["email"]
       bloodgroup=request.POST["bloodgroup"]
       age=request.POST["age"]
       mobile=request.POST["mobile"]
       password=request.POST["password"]
       village=request.POST["village"]
       mandal=request.POST["mandal"]
       pincode=request.POST["pincode"]
       if Donors.objects.filter(email=email).exists():
           messages.info(request,"User already exists")
           return render(request,"register.html")
       else:
           d=Donors.objects.create(name=name,email=email,bloodgroup=bloodgroup,age=age,password=password,number=mobile,village=village,mandal=mandal,pincode=pincode)
           d.save()
           messages.success(request, 'Successfully Register!')
           return render(request,"home.html")
    else:
        return render(request,"register.html")

def edit(request):
    global obj
    if request.method == "POST":
       obj.name=request.POST["name"]
       obj.email=request.POST["email"]
       obj.bloodgroup=request.POST["bloodgroup"]
       obj.age=request.POST["age"]
       obj.mobile=request.POST["mobile"]
       obj.village=request.POST["village"]
       obj.mandal=request.POST["mandal"]
       obj.pincode=request.POST["pincode"]
       obj.save()
       return render(request,"profile.html",{"object":obj})
    else:
       return render(request,"edit.html",{"object":obj})

def photoedit(request):
    if 'image' in request.FILES:
       global obj
       obj.photo.delete(save=True)
       obj.photo=request.FILES["image"]
       obj.save()
    return render(request,"edit.html",{"object":obj})
    

def donate(request):
    if request.method=="POST":
      def inactive(obj):
        obj.status="False"
        obj.save()
      def active(obj):
        obj.status="True"
        obj.save() 
      global obj
      if "active" in request.POST:
        inactive(obj)
        messages.success(request, 'your are now inactive status')
      elif "inactive" in request.POST:
        if obj.status=="True":
          messages.info(request,"Already active status")
        else:
          active(obj)
          messages.success(request, 'Thankyou for showing interest to donate')
    return render(request,"donate.html",{"object":obj})
def reset(request):
   if request.method=="POST":
      global obj
      p1=request.POST["password1"]
      p2=request.POST["password2"]
      if p1==p2:
        obj.password=p1
        obj.save()
        messages.success(request,"changes successfull")
      else:
        messages.info(request,"Passwords does not match")
   return render(request,"resetpassword.html")


def forgot(request):
  if request.method=="POST":
    global OTP
    if "otp" in request.POST:
      userid=request.POST["email"]
      if Donors.objects.filter(email=userid).exists():
          user=Donors.objects.get(email=userid)
          digits = "0123456789"
          OTP=""
          for i in range(6) :
              OTP += digits[math.floor(random.random() * 10)]
          subject = 'Login OTP'
          d={'object':user,'OTP':OTP}
          content = render_to_string("email.html",context=d)
          email_from = settings.EMAIL_HOST_USER
          recipient_list = [user.email, ]
          message=EmailMessage(subject, content, email_from, recipient_list )
          message.content_subtype='html'
          message.send()
          return render(request,"otplogin.html",{"email":user.email})
      else:
          messages.info(request,"Invalid Email")
          return render(request,"Otpgenerate.html")

    if "login" in request.POST:
        otp=request.POST["password"]
        userid=request.POST["email"]
        print(OTP)
        user=Donors.objects.get(email=userid)
        if otp == OTP:
            global obj
            obj=user
            return render(request,"userpage.html",{'object':obj})
        else:
          messages.error(request,'Wrong OTP')
          return render(request,"otplogin.html")
  return render(request,"Otpgenerate.html")
    



   


