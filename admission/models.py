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
    role = models.CharField(max_length=100, default="default")
    pic = models.ImageField(upload_to="facultypics/")
    faculty_department = models.TextField(default="department details")
    faculty_description = models.TextField(default="description details")

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    short_code = models.CharField(max_length=20)
    description = models.TextField(default="course details")


    def __str__(self):
        return self.name


class YoutubeLink(models.Model):
    video_title = models.TextField(default="enter title here")
    youtube_video_url = models.URLField()

    def __str__(self):
        return self.video_title


class Podcast(models.Model):
    front_img = models.ImageField(upload_to="podcastpics/", null=True)
    title = models.CharField(max_length=100)
    text = models.TextField(default="enter text keep it a maximum of 2 lines")
    spotify_podcast_link = models.URLField(null=True)
    google_podcast_link = models.URLField(null=True)
    apple_podcast_link = models.URLField(null=True)

    def __str__(self):
        return self.title


class PhotoGallery(models.Model):
    pic_in_gallery = models.ImageField(upload_to="gallerypics/")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question


class Certificateintheology(models.Model):
    brief = models.TextField(default="write about course in brief and only add data once ")
    entry_requirements = models.TextField(default="entry requirements")
    Period_of_study = models.TextField(default='enter details about period of study')
    curriculum = models.TextField(default="enter details about curriculum")
    class Meta:
        verbose_name_plural = "Certificates in Theology"
    def __str__(self):
        return "this is the only item needed donot add more"

class Bachelorsintheology(models.Model):
    brief = models.TextField(default="write about course in brief and only add data once ")
    # Fields go here
    entry_requirements = models.TextField(default="entry requirements")
    Period_of_study = models.TextField(default='enter details about period of study')
    curriculum = models.TextField(default="enter details about curriculum")

    class Meta:
        verbose_name_plural = "Bachelors in Theology"
    def __str__(self):
        return "this is the only item needed donot add more"

class Diplomointheology(models.Model):
    # Fields go here
    brief = models.TextField(default="write about course in brief and only add data once ")
    entry_requirements = models.TextField(default="entry requirements")
    Period_of_study = models.TextField(default='enter details about period of study')
    curriculum = models.TextField(default="enter details about curriculum")

    class Meta:
        verbose_name_plural = "Diplomo in Theology"
    def __str__(self):
        return "this is the only item needed donot add more"

class MastersinDivinity(models.Model):
    brief = models.TextField(default="write about course in brief and only add data once ")
    entry_requirements = models.TextField(default="entry requirements")
    Period_of_study = models.TextField(default='enter details about period of study')
    curriculum = models.TextField(default="enter details about curriculum")


    class Meta:
        verbose_name_plural = "Masters in Divinity"
    def __str__(self):
        return "this is the only item needed donot add more"