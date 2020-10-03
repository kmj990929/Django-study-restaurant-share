from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

def index(request):
    #return HttpResponse("index")
    categories = Category.objects.all()
    content = {'categories':categories}
    return render(request, 'shareRes/index.html', content)

def restaurantDetail(request):
    #return HttpResponse("restaurantDetail")
     return render(request, 'shareRes/restaurantDetail.html')

def restaurantCreate(request):
    #return HttpResonse("restaurantCreate")
    return render(request, 'shareRes/restaurantCreate.html')

def categoryCreate(request):
    #return HttpResponse("categoryCreate")
    categories = Category.objects.all()
    content = {'categories' : categories}
    
    return render(request, 'shareRes/categoryCreate.html')

def Create_category(request):
    #return HttpResponse("여기서 category create 기능 구현할거다.")
    category_name = request.POST['categoryName']
    new_category = Category(category_name = category_name)
    new_category.save()
    return HttpResponseRedirect(reverse('index'))