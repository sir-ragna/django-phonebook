from django import forms

class NewPhoneRecordForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label="Name")
    number = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label="Number")
