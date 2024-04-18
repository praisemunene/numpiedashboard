"""
URL configuration for pesheysms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index" ),
    path('404',views.error, name="404" ),
    path('settings',views.changepassword, name="settings" ),
    path('creategroup',views.creategroup, name="creategroup" ),
    path('failapi',views.failapi, name="failapi" ),
    path('forgotpassword',views.forgotpassword, name="forgotpassword" ),
    path('login',views.login, name="login" ),
    path('managegroup',views.managegroup, name="managegroup" ),
    path('misreport',views.misreport, name="misreport" ),
    path('pay',views.pay, name="pay" ),
    path('register',views.register, name="register" ),
    path('senderid',views.senderid, name="senderid" ),
    path('sendsms',views.sendsms, name="sendsms" ),
    path('smspersonalised',views.smspersonalised, name="smspersonalised" ),
    path('smsstatus',views.smsstatus, name="smsstatus" ),
    path('templates',views.templates, name="templates" ),
    path('ussd/',views.ussd, name="ussd/"),
    path('registration/', views.registration, name='registration'),
    path('loginform/', views.loginform, name='loginform'),
    path('logout', views.logout, name='logout'),
    path('uploadgroup/', views.uploadcsv, name='uploadgroup'),
    path('getuserdata', views.getuserdata, name='getuserdata'),
    path('changemypassword', views.changemypassword, name='changepassword'),
    path('applysenderid', views.applysenderid, name='applysenderid'),
    path('getsenderids', views.getsenderids, name='getsenderids'),
    path('invoice', views.invoice, name='invoice'),
    path('updateprofile', views.updateprofile, name='updateprofile'),
]
