from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.forms import *


def Student_Display(request):
    SO=StudentForm()
    d={'SO':SO}
    if request.method=='POST':
        SD=StudentForm(request.POST)
        if SD.is_valid():
            return HttpResponse('its a valid data')
        else:
            return HttpResponse('not a valid data')
    return render(request,'StudentForm.html',d)
    