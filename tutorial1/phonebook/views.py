from django.http import HttpResponse
from django.shortcuts import render

from phonebook.models import PhoneRecord

def index(request):
    new_phone_record = PhoneRecord("1234", "John")
    new_phone_record.save()

    all_records = PhoneRecord.objects.all()

    #return HttpResponse("<h1>Hello world</h1>")
    return render(request, "frontpage.html.j2", 
        { "phone_records" : all_records }
    )
