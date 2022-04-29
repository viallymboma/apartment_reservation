from django.shortcuts import render
from .models import Catalogue, Testimonial
from rooms.models import Appartment

# Create your views here.

def index (request):
    rooms= Appartment.objects.all()
    catalogues= Catalogue.objects.all()
    testimonials = Testimonial.objects.all()

    contex = {
        'catalogues': catalogues, 
        'testimonial': testimonials,
        'rooms': rooms
    }

    return render(request,'index.html', contex)

def contact(request):
    return  render (request, "contact.html")

def blog (request):
    rooms = Chambre.objects.all()
    return render (request, "blog.html",{'rooms': rooms})

def about(request):
    return render (request, 'about.html')
