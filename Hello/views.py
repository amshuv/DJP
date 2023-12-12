from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .forms import studentform
from .models import students
# Create your views here.
form = studentform()
my_dict = {"insert_me": "Its lowest...", "sr": "Star dust", 'n': 300,'form': form}
def index(request):
    return HttpResponse("<h1> I started learning Django and its FUN </h1>")

def Hello(request):
    # return HttpResponse("<h2>I am coming from the application urls.py file</h2>")
    if request.method == "POST":
        form = studentform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = studentform()
    return render(request, 'Hello/Home.html', context=my_dict)

# def amshu(request):
#     return HttpResponse("<marquee>i am done</marquee>")

def list_view(request):
    # dictionary for initial data with field name as keys
    context={}
    # add the dictionary during initialization
    context["dataset"] = students.objects.all()
    return render(request, 'Hello/list_view.html', context)