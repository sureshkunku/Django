from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Employee
import datetime

# Create your views here.


def Test_Method(request):
    return  HttpResponse('<h1> Hello Suresh, your first project is created sucessfuly with out any error</h1>')

def New_test(request):
    dt=datetime.datetime.now()
    my_dic={'Name':"Suresh",'date':dt}
    s=render(request,'testapp/result.html',my_dic)
    return s
def employee_view(request):
    emp=Employee.objects.all()
    return render(request,'testapp/result.html',{'emp':emp})



