from django.shortcuts import render

# Create your views here.

def helloWorld(request, *args, **kwargs):
    return render(request, "blog/helloWorld.html")