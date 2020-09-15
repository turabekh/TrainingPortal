from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import Course
from lessons.models import Step


def home(request):
    return HttpResponse("<h1>Home Course Page</h1>")


class CourseDetailView(DetailView):
    model = Course 
    slug_field = "slug"
    slug_url_kwarg = "slug"
    

def step_detail(request, topic_slug, slug):
    step = get_object_or_404(Step,slug=slug)
    return render(request, "courses/step_detail.html", {"step": step})