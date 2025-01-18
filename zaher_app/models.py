from django.db import models

# Create your models here.
class AboutUs(models.Model):
    company_name = models.CharField(max_length=200, blank=True, null=True)
    company_activity = models.TextField(max_length=1000)
    current_activity = models.CharField(max_length=500)
    workforce = models.CharField(max_length=500)
    company_locations = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='about/', blank= True, null=True)
    def __str__(self):
        return self.current_activity

    class Meta:
        verbose_name_plural = "About Us"
        
class Slider(models.Model):
    image = models.ImageField(upload_to='slider-images/')
    title = models.CharField(max_length=100, blank=True, null= True)
    short_description = models.CharField(max_length=200)

    def __str__(self):
        return self.short_description



class CompanyInfo(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logo/')
    headquarter_address = models.CharField(max_length=300)
    main_warehouse_address = models.CharField(max_length=300)
    maintenance_center_address = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Company Info"


class ContactInfo(models.Model):
    administration_number = models.CharField(max_length=20)
    workshop_number = models.CharField(max_length=20)
    sales_number = models.CharField(max_length=20)
    mail = models.CharField(max_length=50, blank=True, null=True)
    opening_day = models.CharField(max_length=50, blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    closing_day = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Contact Info"


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='service-images/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Services"
