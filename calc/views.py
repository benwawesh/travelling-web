from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request, 'home.html',{"name":"benson"})
def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    ans=val1 + val2
    return render(request, 'add.html',{"answer":ans})
