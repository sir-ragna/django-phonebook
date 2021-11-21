from django.http import HttpResponse
from django.shortcuts import render

from phonebook.models import PhoneRecord

def index(request):
    
    PhoneRecord.objects.all().delete() # remove all objects

    # Create new user John
    new_phone_record = PhoneRecord(name="John", number="12346")
    new_phone_record.save()

    # Create new user Mary
    new_phone_record = PhoneRecord(name="Marry", number="00607")
    new_phone_record.save()

    all_records = PhoneRecord.objects.all()

    #return HttpResponse("<h1>Hello world</h1>")
    return render(request, "frontpage.html.j2", 
        { "phone_records" : all_records }
    )
