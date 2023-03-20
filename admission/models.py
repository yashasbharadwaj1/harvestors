from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Apply(models.Model):
    application_recieved = 'ar'
    contacted = 'co'
    not_contacted = 'nc'
    selected = 'se'
    rejected = 're'
    Choices = [
        (application_recieved, 'application_recieved'),
        (contacted, 'contacted'),
        (not_contacted, 'not_contacted'),
        (selected, 'selected'),
        (rejected, 'rejected'),
    ]
    certificate_in_theology = 'Cth'
    diploma_in_theology = 'Dth'
    bachelor_in_theology = 'Bth'
    masters_in_divinity = 'MD'

    course_choices = [
        (certificate_in_theology, 'certificate_in_theology'),
        (diploma_in_theology, 'diploma_in_theology'),
        (bachelor_in_theology, 'bachelor_in_theology'),
        (masters_in_divinity, 'masters_in_divinity'),

    ]
    email = models.EmailField()
    name = models.CharField(max_length=150)
    birth_date = models.DateField()
    phonenum = PhoneNumberField()
    course_interested = models.CharField(
        max_length=150,
        choices=course_choices,
        default=certificate_in_theology
    )
    status = models.CharField(
        max_length=2,
        choices=Choices,
        default=application_recieved,
    )

    def __str__(self):
        return self.name


class InformationRequests(models.Model):
    email = models.EmailField()
    query_box = models.TextField()

    def __str__(self):
        return f"Information Request => {self.id}"


class Alumni(models.Model):
    name = models.CharField(max_length=100)
    pic = models.ImageField(upload_to="alumniimages/")
    alumni_talk = models.TextField()

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    pic = models.ImageField(upload_to="facultypics/")
    faculty_description = models.TextField()

    def __str__(self):
        return self.name
