from django.urls import path

from .views import index, meetup_details

urlpatterns = [
    path("meetups/", index, name="index"), # our-domain.com/meetups
    path("meetups/<slug:meetup_slug>/", meetup_details, name="meetup-details"), # our-domain.com/meetups/a-first-meetup   
]