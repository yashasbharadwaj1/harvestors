app_name = "posting"
from django.urls import path
from .views import *

urlpatterns = [

    path('academics/', academicspost, name='acadpost'),
    path('events/', eventspost, name='eventspost'),
    path('courses/', coursespost, name='coursespost'),
    path('<slug:post>/', post_single, name='post_single'),
]
