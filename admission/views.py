from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
# Create your views here.
from .forms import applyform, requestinfoform
from .models import *

from .utils import calculate_age
from rest_framework.decorators import api_view

from .serializers import *

import requests
from django.urls import reverse



def robots_txt(request):
    content = "User-agent: *\nDisallow:\nSitemap: https://www.harvesterstheologicalseminary.org/sitemap.xml"
    return HttpResponse(content, content_type="text/plain")

@api_view(["GET"])
def support(request):
    apply_objs = Apply.objects.all()
    serialized = ApplySerializer(data=apply_objs)
    if not serialized.is_valid():
        ordered_dict = serialized.data
        json_str = json.dumps(ordered_dict)
        status_dict = json.loads(json_str)

    return JsonResponse(data={"d": "d"})


def t(request):
    url = reverse('posting:eventspost')
    response = requests.get(request.build_absolute_uri(url))  # Build the full URL

    data = response.json()  # dict which contans dictionary
    for i in data["output"]:
        print(i["title"])
    return HttpResponse("t")


def sitemap(request):
    return render(request, 'sitemap.html')


def home(request):
    url_for_recentevents = reverse('posting:eventspost')
    response = requests.get(request.build_absolute_uri(url_for_recentevents))  # Build the full URL
    recentevents = response.json()  # dict which contans dictionary

    url_for_coursedetails = reverse('admission:course_details')
    coursedetailsresponse = requests.get(request.build_absolute_uri(url_for_coursedetails))
    coursedetails = coursedetailsresponse.json()

    y = YoutubeLink.objects.all()

    s = Slider.objects.all()
    # 3 things need to be updated recent events,courses offered,youtube links
    context = {"recentevents": recentevents, "coursedetails": coursedetails, "y": y,"s":s}
    return render(request, 'index.html', context)


def podcast(request):
    podcast_dataurl = reverse("admission:data_for_podcast")
    podcastresponse = requests.get(request.build_absolute_uri(podcast_dataurl))
    datapodcast = podcastresponse.json()
    context = {"datapodcast": datapodcast}
    return render(request, 'podcast.html', context)


@api_view(["GET"])
def data_for_podcast(request):
    podcast_objs = Podcast.objects.all()
    serialized = PodcastSerializer(data=podcast_objs, many=True)
    if not serialized.is_valid():
        ordered_dict = serialized.data
        json_str = json.dumps(ordered_dict)
        podcast_dict = json.loads(json_str)

    return JsonResponse(data={"podcastdata": podcast_dict})


def photogallery(request):
    photogallery_url = reverse('admission:gallerydata')
    galleryresponse = requests.get(request.build_absolute_uri(photogallery_url))
    gallerydata = galleryresponse.json()
    context = {"gallerydata": gallerydata}
    return render(request, 'gallery.html', context)


@api_view(["GET"])
def data_for_photogallery(request):
    gallery_objs = PhotoGallery.objects.all()
    serialized = PhotoGallerySerializer(data=gallery_objs, many=True)
    if not serialized.is_valid():
        ordered_dict = serialized.data
        json_str = json.dumps(ordered_dict)
        gallery_dict = json.loads(json_str)

    return JsonResponse(data={"gallerydata": gallery_dict})


def placementcell(request):
    return render(request, 'placementcell.html')


def visit(request):
    return render(request, 'visit.html')


def aboutus(request):
    allfacultyobjs = Faculty.objects.all()
    textcontent = Aboutpagecontent.objects.all()
    context = {'all': allfacultyobjs,'textcontent':textcontent}
    return render(request, 'aboutus.html', context)


# this is giving info regarding C.th
def certificateinth(request):
    cth = Certificateintheology.objects.all()
    return render(request, 'cth.html', {"cth": cth})


def diplomainth(request):
    dth = Diplomointheology.objects.all()
    return render(request, 'dipth.html', {"dth": dth})


def bachelorinth(request):
    bth = Bachelorsintheology.objects.all()
    return render(request, 'bth.html', {"bth": bth})


def mastersindivinity(request):
    mdiv = MastersinDivinity.objects.all()
    return render(request, 'mdiv.html', {"mdiv": mdiv})


def donate(request):
    return render(request, 'donate.html')


def thanks(request):
    return render(request, 'thanks.html')


def applyview(request):
    if request.method == "POST":
        form = applyform(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            birth_date = form.cleaned_data["birth_date"]
            phone_number = form.cleaned_data["phone_number"]
            course_interested = form.cleaned_data["course_interested"]
            person_age_year = calculate_age(birth_date.day, birth_date.month, birth_date.year)

            queryset = Apply.objects.all()

            for obj in queryset:
                if obj.name == name:
                    return HttpResponse("name already taken")
                elif obj.email == email:
                    return HttpResponse("email already in use")
                elif obj.phonenum == phone_number:
                    return HttpResponse('phonenum already exists')

                elif person_age_year < 16 or person_age_year > 80:
                    return HttpResponse(
                        'u are only allowed when your age is greater than or equal 16 and less than or equal to 80')

            # print(birth_date.year) ex:1954
            # print(birth_date.day) ex:1
            # print(birth_date.month) ex:2 feb

            Apply.objects.create(name=name, email=email, birth_date=birth_date, phonenum=phone_number,
                                 course_interested=course_interested[0])

            return render(request, 'applysuccess.html')

        else:
            return HttpResponse("an indian phone number contains only 10 digits u need not include 91 at start "
                                "or enter more than 10 digits")

    if request.method == "GET":
        form = applyform()
        context = {'f': form}
        return render(request, 'apply.html', context)


def requestinfo(request):
    if request.method == "GET":
        form = requestinfoform()
        context = {"f": form}
        return render(request, 'requestinfo.html', context)

    elif request.method == "POST":
        form = requestinfoform(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            query_box = form.cleaned_data['query_box']

            # print(email)
            # print(query_box)
            InformationRequests.objects.create(email=email, query_box=query_box)

            return HttpResponse('your query taken our team will reply to you through mail')
        else:
            return JsonResponse(data={"errors": form.errors})


def admissionfaq(request):
    faq = Faq.objects.all()
    a =AdmissionPagecontent.objects.all()
    return render(request, 'admission.html', {"faq": faq,"a":a})

def statementofbelief(request):
    obj = StatementOfBelief.objects.all()
    return render(request, 'statementofbelief.html', {'a': obj})

def list_alumni(request):
    allalumniobjs = Alumni.objects.all()
    return render(request, 'listalumni.html', {'all': allalumniobjs})


# this view is for all faculties from faculty button
def list_faculties(request):
    allfacultyobjs = Faculty.objects.all()
    return render(request, 'listfaculties.html', {'all': allfacultyobjs})


# courses offered in index.html rest-api endpoint
@api_view(["GET"])
def course_details(request):
    if request.method == "GET":
        course_objs = Course.objects.all()
        serialized = CourseSerializer(data=course_objs, many=True)

        if not serialized.is_valid():
            ordered_dict = serialized.data
            # json.dumps to Serialize obj to a JSON formatted str.
            json_str = json.dumps(ordered_dict)
            # json.loads to Deserialize s (a str, bytes or bytearray instance containing a JSON document) to a Python object.
            my_dict = json.loads(json_str)
            context = {"coursedata": my_dict}
        return JsonResponse(data=context)

# about us faculties needs only pic,name,department rest api endpoint
