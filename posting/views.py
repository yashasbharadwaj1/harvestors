from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post, Category
from .serializers import PostSerializer
# Create your views here.
from django.db.models import Q
from rest_framework.decorators import api_view
import json
import re


def academicspost(request):
    query = Q()
    o = Category.objects.get(name="academics")
    # print(o)
    query &= Q(category=o)
    acad_posts = Post.objects.all().filter(query)

    return render(request, 'academics.html', {"a": acad_posts})


import unicodedata


@api_view(["GET"])
def eventspost(request):
    if request.method == 'GET':
        query = Q()
        o = Category.objects.get(name="events")
        # print(o)
        query &= Q(category=o)
        latest3_events_objs = Post.objects.all(). \
                                  filter(query).order_by('-publish')[:3]
        serialized = PostSerializer(data=latest3_events_objs, many=True)

        if not serialized.is_valid():
            ordered_dict = serialized.data
            # print(ordered_dict)
            json_str = json.dumps(ordered_dict)
            # print(json_str)
            my_dict = json.loads(json_str)
            # print(my_dict)
            # print(type(my_dict)) - list
            # print(type(my_dict[0])) - dict

        for item in my_dict:
            # Replace Unicode apostrophes with regular apostrophes in title and excerpt
            item['title'] = unicodedata.normalize('NFKD', item['title']).encode('ascii', 'ignore').decode('utf-8')
            item['summary'] = unicodedata.normalize('NFKD', item['summary']).encode('ascii', 'ignore').decode('utf-8')
            item['publish'] = item['publish'][:10]
            # url to render post single http://127.0.0.1:8000/data/slug/

        context = {"output": my_dict}

        return JsonResponse(data=context)

    else:
        return JsonResponse(data={"status": "only get method allowed"})


def coursespost(request):
    query = Q()
    o = Category.objects.get(name="course")
    query &= Q(category=o)
    courses_posts = Post.objects.all().filter(query)
    return render(request, 'courses.html', {'c': courses_posts})


def post_single(request, post):
    post = get_object_or_404(Post, slug=post)
    return render(request, 'postsingle.html', {'post': post})
