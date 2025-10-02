from django.urls import path

from .views import index, meetup_details, confirm_registration

urlpatterns = [
    path("", index, name="index"), # our-domain.com/meetups
    path("<slug:meetup_slug>/success/", confirm_registration, name="confirm-registration"), # our-domain.com/meetups/success   
    path("<slug:meetup_slug>/", meetup_details, name="meetup-details"), # our-domain.com/meetups/a-first-meetup   
]