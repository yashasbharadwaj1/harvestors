from django.db import models
from .models import *
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone

# models for handling events,achievements,announcements

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Post(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)

    title = models.CharField(max_length=250)
    # excerpt is like a short description of ur main content
    excerpt = models.TextField(null=True)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body= RichTextUploadingField(blank=False)
    status = models.CharField(max_length=10, choices=options, default='draft')
    publish = models.DateTimeField(default=timezone.now)

    newmanager = NewManager()  # custom manager
    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('post:post_single', args=[self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
# Create your models here.
