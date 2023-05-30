from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from .models import *
import numpy as np
import tensorflow as tf
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Create your views here.
def Loginpage(request):
    return render(request,"login.html")

def Userlogin(request):
    if request.method=="POST":
        uname=request.POST['mail']
        password=request.POST['password']

        user=User.objects.filter(username=uname)
        if user:
            user=auth.authenticate(username=uname,password=password)
            if user:
                auth.login(request,user)
                if user.is_superuser==1:
                    return redirect('adminpage')
                elif user.is_superuser==2:
                    return redirect('doctor')
                else:
                    return redirect('userpage')
            else:
                message="Password is Wrong"
                return render(request,"login.html",{'msg':message})
        else:
            message="Not a Member do register"
            return render(request,"login.html",{'msg':message})


   
def Userlogout(request):
    auth.logout(request)
    message="Successfully Logout"
    return render(request,"login.html",{'msg':message})

@login_required(login_url='')
def Adminpage(request):
    user = request.user
    message = "Successfully Login"
    admin=User.objects.get(username=user)
    all_data=User.objects.all()
    return render(request,"adminpage.html",{'msg': message, 'user': user,'data':all_data,'admin':admin})

@login_required(login_url='')
def doctor(request):
    user = request.user
    message = "Successfully Login"
    dr=User.objects.get(username=user)
    all_data=User.objects.all()
    return render(request,"doctor.html",{'msg': message, 'user': user,'data':all_data,'admin':dr})


@login_required(login_url='')
def Userpage(request):
    user = request.user 
    message="Successfully Login"
    all_data=User.objects.get(username=user)
    return render(request,'userpage.html',{'msg':message,'user':user,'data':all_data})

def Registerpage(request):
    return render(request,"registerpage.html")

def Userregister(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        mail=request.POST['mail']
        uname=request.POST['mail']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

    user=User.objects.filter(email=mail)

    if user:
        message="User Already Register"
        return render(request,"login.html",{'msg':message})
    else:
        if password == cpassword:
            if len(password)>=8:
                newuser=User.objects.create_user(first_name=fname,last_name=lname,email=mail,password=password,username=uname)
                newuser.save()
                message="User Successfully Registered"
                return render(request,"login.html",{'msg':message})
            else:
                message="small"
                return render(request,"registerpage.html",{'msg':message})
        else:
            message="reg"
            return render(request,"registerpage.html",{'msg':message})
        

@login_required(login_url='')
def Storedandpredict(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        age=request.POST['age']
        gender=request.POST['gender']
        contact=request.POST['phone']
        mail=request.POST['mail']
        check=request.POST['check']
        uname=request.POST['uname']
        symp1=request.POST['symp1']
        symp2=request.POST['symp2']
        symp3=request.POST['symp3']
        symp4=request.POST['symp4']
        symp5=request.POST['symp5']
        symp6=request.POST['symp6']
        symp7=request.POST['symp7']
        symp8=request.POST['symp8']
        pics=request.FILES['image']


        model = load_model('static/best_model.h5')

        inputimg = Image.open(pics)
        inputimg = inputimg.resize((28, 28))
        img = np.array(inputimg).reshape(-1, 28, 28, 3)
        result = model.predict(img)
        
        result = result.tolist()
        max_prob = max(result[0])
        class_ind = result[0].index(max_prob)
        class_labels = ['actinic keratoses and intraepithelial carcinomae(Cancer)',
                         'basal cell carcinoma(Cancer)',
                         'benign keratosis-like lesions(Non-Cancerous)',
                         'dermatofibroma(Non-Cancerous)',
                         'melanocytic nevi(Non-Cancerous)',
                         'pyogenic granulomas and hemorrhage(Can lead to cancer)',
                         'melanoma(Cancer)']
        predicted_label = class_labels[class_ind]

        prediction_data=Recordresult.objects.create(username=uname,firstname=firstname,lastName=lastname,age=age,contact=contact,gender=gender,Image=pics,symp1=symp1,symp2=symp2,symp3=symp3,symp4=symp4,symp5=symp5,symp6=symp6,symp7=symp7,symp8=symp8,is_check=check,Predicteddegree=predicted_label)
        return redirect('viewuserdetails',uname=uname)

def adminresult(request,uname):
    all_data=Recordresult.objects.filter(username=uname).order_by('-id')
    return render(request,"adminresult.html",{'value':all_data})

def doctorresult(request,uname):
    all_data=Recordresult.objects.filter(username=uname).order_by('-id')
    return render(request,"doctorresult.html",{'value':all_data})

def userview(request, pk):
    updatedata = Recordresult.objects.get(id=pk)
    updatedata.suggestion=request.POST['suggestion']
    updatedata.is_check=request.POST['is_check']
    updatedata.save()
    return redirect('doctor')

def Viewuserdetails(request,uname):
    all_data=Recordresult.objects.filter(username=uname,is_check=False).order_by('-id')
    return render(request,"userinfo.html",{'value':all_data})

def Viewdetails(request,pk):
    all_data=Recordresult.objects.get(id=pk)
    return render(request,"viewdetailed.html",{'value':all_data})


def Back(request):
    return redirect('loginpage')






