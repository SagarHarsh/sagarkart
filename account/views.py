from django.shortcuts import render

# Create your views here.

def Home(request):
    return  render(request,'account/home1.html')

def Orders (request):
    return  render(request,'account/order1.html')

def Help(request):
    return  render(request,'account/help.html')