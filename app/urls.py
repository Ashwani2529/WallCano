from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path("",views.index,name='app'),
    path("a/",views.about,name='about'),
    path("c/",views.contact,name='contact')
]
