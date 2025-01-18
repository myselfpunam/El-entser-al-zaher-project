from django.contrib import admin
from .models import *

admin.site.site_title = "EL-ENTISAR AL ZAHER" 
admin.site.site_header = "EL-ENTISAR AL ZAHER"  
admin.site.index_title = "Welcome to the EL-ENTISAR AL ZAHER Dashboard" 
# Register your models here.
admin.site.register(AboutUs)
admin.site.register(Slider)
admin.site.register(CompanyInfo)
admin.site.register(ContactInfo)
admin.site.register(Service)
