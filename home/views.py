from django.shortcuts import render, HttpResponse

# Create your views here.
# URL dispatching


def index(request):
    context = {
        "variable": "this is sent"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is Homepage")


def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is Aboutpage")


def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is Servicespage")


def contact(request):
    return render(request, 'contact.html')
    #return HttpResponse("This is Contactpage")
