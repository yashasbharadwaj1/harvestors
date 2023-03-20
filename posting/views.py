from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post, Category

# Create your views here.
from django.db.models import Q


def academicspost(request):
    query = Q()
    o = Category.objects.get(name="academics")
    #print(o)
    query &= Q(category=o)
    query &= Q(status ='published')
    acad_posts = Post.objects.all().filter(query)

    return render(request, 'academics.html',{"a":acad_posts})


def eventspost(request):
    query = Q()
    o = Category.objects.get(name="events")
    #print(o)
    query &= Q(category=o)
    query &= Q(status ='published')
    events_posts = Post.objects.all().filter(query)

    return render(request, 'events.html',{'e':events_posts})

def coursespost(request):
    query = Q()
    o = Category.objects.get(name="course")
    query &= Q(category=o)
    query &= Q(status ='published')
    courses_posts = Post.objects.all().filter(query)
    return  render(request,'courses.html',{'c':courses_posts})


def post_single(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    return render(request, 'postsingle.html', {'post': post})
