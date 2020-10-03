# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 23:20:54 2020

@author: kmj99
"""

#shareRes > urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('restaurantDetail/', views.restaurantDetail),
    path('restaurantCreate/', views.restaurantCreate),
    path('categoryCreate/',views.categoryCreate),    
    path('categoryCreate/create',views.Create_category, name = 'cateCreate'),
]