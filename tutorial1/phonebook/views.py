from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from phonebook.models import PhoneRecord
from phonebook.forms import NewPhoneRecordForm

def new_phone_record(request):
    new_record_form = NewPhoneRecordForm(request.POST)
    if new_record_form.is_valid():
        name = new_record_form.cleaned_data["name"]
        number = new_record_form.cleaned_data["number"]

        if len(PhoneRecord.objects.filter(name=name)) == 0:
            # Add to the database
            PhoneRecord(name=name, number=number).save()
        else:
            # Already exists TODO give some user feedback
            pass
    
    # TODO user feedback about success or failure of saving the record

    # redirect to the main page
    return HttpResponseRedirect(reverse('index'))

def index(request):
    
    # PhoneRecord.objects.all().delete() # remove all objects

    # # Create new user John
    # new_phone_record = PhoneRecord(name="John", number="12346")
    # new_phone_record.save()

    # # Create new user Mary
    # new_phone_record = PhoneRecord(name="Marry", number="00607")
    # new_phone_record.save()

    all_records = PhoneRecord.objects.all()
    #PhoneRecord.objects.filter(name="john")

    new_records_form = NewPhoneRecordForm()

    return render(request, "frontpage.html.j2", 
        { 
          "phone_records" : all_records, 
          "new_records_form": new_records_form 
        }
    )
