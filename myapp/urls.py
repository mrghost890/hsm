from unicodedata import name
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('patient/',views.patient,name='patient'),
    path('userprofile/',views.userprofile,name='userprofile'),
    path('updateuserprofile/',views.updateuserprofile,name='updateuserprofile'),
    path('appointment/',views.appointment,name='appointment')
]