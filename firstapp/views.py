from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("hey his name is mukesh")

def detail(request):
     return HttpResponse("It is his original name")
# Create your views here.
