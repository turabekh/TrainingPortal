from django.urls import path
from .views import CourseDetailView
from . import views

urlpatterns = [
    path('', views.home, name="courses-home"),
    path("<slug:topic_slug>/<slug:slug>/", views.step_detail, name="step-detail"),
    path('<slug:slug>/', CourseDetailView.as_view() , name='course-detail'),

]
