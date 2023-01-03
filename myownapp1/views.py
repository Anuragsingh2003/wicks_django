from operator import index
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index1(request):
    return render(request,'index.html')



def feedback(request):
    return render(request,'feedback.html')



def checkoutbuy(request):
    return render(request,'checkoutbuy.html')


def login(request):
    return render(request,'login.html')

def registration(request):
    return render(request,'registration.html')    



def mission1(request):
    return render(request,'mission1.html')


def confirmation(request):
    return render(request,'confirmation.html')











def myapk(request):
    return HttpResponse('<h1> welcome vro to ours f1 gen apksoft</h1>')



 