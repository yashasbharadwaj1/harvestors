from django.contrib import admin
from .models import Apply,InformationRequests,Alumni,Faculty
# Register your models here.
admin.site.register(Apply)
admin.site.register(InformationRequests)
admin.site.register(Alumni)
admin.site.register(Faculty)
