from django.urls import path
from . import views

urlpatterns = [
    path('',views.Loginpage,name='loginpage'),
    path('userlogin',views.Userlogin,name='userlogin'),
    path('registerpage',views.Registerpage,name='registerpage'),
    path('userrgister',views.Userregister,name='userregister'),
    path('userpage',views.Userpage,name='userpage'),
    path('userlogout',views.Userlogout,name='userlogout'),
    path('adminpage',views.Adminpage,name='adminpage'),
    path('storedandpridicted',views.Storedandpredict,name='storedandpredicted'),
    path('viewuserdetails<str:uname>',views.Viewuserdetails,name='viewuserdetails'),
    path('back',views.Back,name='back'),
    path('adminresult<str:uname>',views.adminresult,name='adminresult'),
    path('doctorresult<str:uname>',views.doctorresult,name='doctorresult'),
    path('doctor',views.doctor,name='doctor'),
    path('userview/<int:pk>',views.userview,name='userview'),
    path('viewdetails/<int:pk>',views.Viewdetails,name='viewdetails'),
]