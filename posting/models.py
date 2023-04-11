from django.db import models
from .models import *
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone

# models for handling events,achievements,announcements

from django.core.exceptions import ValidationError

def validate_word_count(value):
    if len(value.split()) > 30:
        raise ValidationError('Too many words! cant enter more than 30 words')

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Post(models.Model):

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)

    title = models.CharField(max_length=250)
    # excerpt is like a short description of ur main content
    summary = models.TextField(null=False,default="summary",  validators=[validate_word_count])
    morecontent = models.TextField(default ="body")
    #should not have gaps,letters etc
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    #body= RichTextUploadingField(blank=False)
    picture = models.ImageField(upload_to="postpics/",default='sli1.jpg')
    publish = models.DateTimeField(default=timezone.now)
    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('post:post_single', args=[self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

