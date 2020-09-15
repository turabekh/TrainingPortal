from django.shortcuts import render
from courses.models import Course, Category


def home(request):
    courses = Course.objects.all()
    context = {
        "courses": courses
    }    

    return render(request, "home/home.html", context=context)

def about(request):
    return render(request, "home/about.html")