# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 23:19:46 2020

@author: kmj99
"""

#sendEmail > urls.py

from django.urls import path, include
from . import views

urlpatterns = [
    path('send/',views.sendEmail)    
]