from django.shortcuts import render

# to return http format
from django.http import HttpResponse

# Create your views here.


def home(request):
    # return HttpResponse("<h1>Hello oliviertech</h1>");
    return render(request,'home.html',{'name':"oliviertech"});

def add(request):
    val1=request.POST["num1"]
    val2=request.POST["num2"]
    result=float(val1)+float(val2)



    return render(request,'result.html',{'result':result})