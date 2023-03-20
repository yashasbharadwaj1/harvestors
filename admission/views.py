from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

# Create your views here.
from .forms import applyform, requestinfoform
from .models import Apply, InformationRequests, Alumni, Faculty

from .utils import calculate_age

def home(request):
    return render(request,'home.html')

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
            phonenum = form.cleaned_data["phonenum"]
            course_interested = form.cleaned_data["course_interested"]
            person_age_year = calculate_age(birth_date.day, birth_date.month, birth_date.year)

            queryset = Apply.objects.all()

            for obj in queryset:
                if obj.name == name:
                    return HttpResponse("name already taken")
                elif obj.email == email:
                    return HttpResponse("email already in use")
                elif obj.phonenum == phonenum:
                    return HttpResponse('phonenum already exists')

                elif person_age_year < 16 or person_age_year > 80:
                    return HttpResponse(
                        'u are only allowed when your age is greater than or equal 16 and less than or equal to 80')

            # print(birth_date.year) ex:1954
            # print(birth_date.day) ex:1
            # print(birth_date.month) ex:2 feb

            Apply.objects.create(name=name, email=email, birth_date=birth_date, phonenum=phonenum,course_interested=course_interested[0])

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




def list_alumni(request):
    allalumniobjs = Alumni.objects.all()
    return render(request, 'listalumni.html', {'all': allalumniobjs})


def list_faculties(request):
    allfacultyobjs = Faculty.objects.all()
    return render(request, 'listfaculties.html', {'all': allfacultyobjs})



