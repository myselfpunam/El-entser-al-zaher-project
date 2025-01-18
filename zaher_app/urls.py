from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = "index"),
    path('services', views.service, name = "service"),
    path('<int:id>', views.serviceDetails, name = "serviceDetails"),
    path('about', views.about, name = "about"),
    path('contact', views.contact, name = "contact"),
    

]
