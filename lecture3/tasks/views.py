from django.shortcuts import render

# Create your views here.
tasks = ["wash the dishes", "do the laundry", "read some pages"]

def index(request):
    return render(request, "tasks/index.html", {"tasks": tasks})

def add(request):
    return render(request, "tasks/add.html")