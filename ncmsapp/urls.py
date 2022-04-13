from django.contrib import admin
from django.urls import path, include
from django.urls.conf import include
from . import views

urlpatterns = [
   path('', views.home, name="home"),
   # path('', views.index, name="index"),
   path('signUp', views.signUp, name="signUp"),
   path('signIn', views.signIn, name="signIn"),
   path('signOut', views.signOut, name="signOut"),
   path('aboutUs', views.aboutUs, name="aboutUs"),
   path('images', views.images, name="images"),
   path('index', views.index, name="index"),
   path('saveenquiry', views.saveEnquiry, name="saveenquiry"),
]
