from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register(request):
    # return render(request, 'index.html')
    name = request.GET.get('name')
    if name:
        return HttpResponse(f"Hello, {name}.")
    
    return HttpResponse("Hello, world.")

    # localhost:8000/register?name=pouya