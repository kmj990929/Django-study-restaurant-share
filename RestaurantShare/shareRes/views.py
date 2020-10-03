from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    #return HttpResponse("index")
    return render(request, 'shareRes/index.html')

def restaurantDetail(request):
    #return HttpResponse("restaurantDetail")
     return render(request, 'shareRes/restaurantDetail.html')

def restaurantCreate(request):
    #return HttpResonse("restaurantCreate")
    return render(request, 'shareRes/restaurantCreate.html')

def categoryCreate(request):
    #return HttpResponse("categoryCreate")
    return render(request, 'shareRes/categoryCreate.html')