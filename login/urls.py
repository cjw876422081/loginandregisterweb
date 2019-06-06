#-*-coding:utf-8-*-
from django.urls import path

from login import admin, views
from login import urls
from captcha import urls

urlpatterns = [
    path('index/' ,views.index ),
    path('login/' , views.login),
    path('register/' , views.register) ,
    path('logout' ,views.logout ) ,
]
