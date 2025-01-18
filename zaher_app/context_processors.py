# context_processors.py
from .models import *

def company_info(request):
    info = CompanyInfo.objects.first()
    contact = ContactInfo.objects.first()
    return {
        'info': info,
        'contact': contact,
    }
