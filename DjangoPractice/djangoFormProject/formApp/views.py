from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from formApp.forms import MHBForm

# Create your views here.

def mhbView (request):
    if request.method == 'POST':
        form = MHBForm (request.POST)
        print (request.POST)
        if form.is_valid():
            number1 = form.cleaned_data['number1']
            number2 = form.cleaned_data['number2']
            result = number1+number2
            return HttpResponse(result)
        else : 
            return HttpResponse('invalid')
    
    if request.method == 'GET':
        form = MHBForm()
        return render (request,'formApp/index.html',{'form': form})
