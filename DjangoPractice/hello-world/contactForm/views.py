from contactForm.models import Contact
from django import http
from django.shortcuts import render
from django.http import HttpResponse

def mhb_response(request):
    return HttpResponse("Hello I'm pouya")
def register (request):
    if request.method == 'GET':
        numberOfSubmittedForms = len(Contact.objects.all())
        return render(request, 'contactForm/signUp.html',{"count":numberOfSubmittedForms})
    elif request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        description = request.POST.get('description')
        contact = Contact.objects.create(first_name=first_name,
                                            last_name=last_name,
                                            email=email,phone=phone,
                                            description=description)
                                            
        return HttpResponse(f"new contact is saved with id: {contact.id} ")
    raise 


# for little projects use json instead of httpresponse
#res = {"mgs": "succcess"}
#        return JsonResponse(res, status=200)
#    return HttpResponse("Invalid request")

def request_name(request):
    # return render(request, 'index.html')
    name = request.GET.get('name')
    if name:
        return HttpResponse(f"Hello, {name}.")
    
    return HttpResponse("Hello, world.")

    # localhost:8000/register?name=pouya
    # PEP-08 naming conventions
