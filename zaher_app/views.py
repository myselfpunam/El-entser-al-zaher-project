from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
  sliders = Slider.objects.all()
  about = AboutUs.objects.first()
  services = Service.objects.all()
  return render (request, "index.html", {
    'sliders' : sliders,
    'about' : about,
    'services' : services,
  })
  
def about(request):
  about = AboutUs.objects.first()
  services = Service.objects.all()
  return render (request, "about.html", {
    'about' : about,
    'services' : services,
  })
  
def contact(request):

  return render (request, "contact.html")
  
def service(request):
  services = Service.objects.all()
  return render (request, "services.html", {
    'services' : services,
  })
  
def serviceDetails(request, id):
  service_details = Service.objects.get(id=id)
  return render (request, "service-details.html", {
    'service_details' : service_details,
  })
