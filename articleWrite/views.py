from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import form as articleForm

# Create your views here.

def articleWritePageInitial(request):
    if request.method == 'POST':
        form = articleForm.article(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        form = articleForm.article()
    return render(request, 'articleWrite.html', {'form':form})