# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 12:35:22 2021

@author: karry
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
]

