from django.urls import path
from . import views

urlpatterns = [
    path("overview/", views.analytics_overview),
    path("countries/", views.analytics_countries),
    path("projects/", views.analytics_projects),
]