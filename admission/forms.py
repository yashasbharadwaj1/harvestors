from django import forms
from .models import Alumni,Apply
from phonenumber_field.formfields import PhoneNumberField
from datetime import date

class applyform(forms.Form):
    # since i came to know lower bound 16 and upper bound is 80

    BIRTH_YEAR_CHOICES = []
    for i in range(1943, 2024):
        BIRTH_YEAR_CHOICES.append(i)

    name = forms.CharField()
    email = forms.EmailField(widget=forms.EmailInput())
    # in database birth_date will go as yyyy-month-date ex- "1981-03-01"
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    # +91 will get automatically appended as (PHONENUMBER_DEFAULT_REGION = "IN") is set in settings.py
    phone_number = PhoneNumberField()
    COURSE_CHOICES = [
        ('Cth', 'Certificate in Theology'),
        ('Dth', 'Diploma in Theology'),
        ('Bth', 'Bachelor in Theology'),
        ('MD', 'Masters in Divinity'),
    ]
    course_interested = forms.ChoiceField(choices=COURSE_CHOICES, widget=forms.RadioSelect())




class requestinfoform(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput())
    query_box = forms.CharField(widget=forms.Textarea())


