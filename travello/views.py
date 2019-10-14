from django.shortcuts import render
from .models import Destination

def index(request):

    dest_list = Destination.objects.all()
    return render(request,'index.html', {'destinations':dest_list})
