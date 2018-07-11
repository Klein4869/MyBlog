from django.shortcuts import render

# Create your views here.
def articleWritePage(request):
    return render(request, "articleWrite.html")