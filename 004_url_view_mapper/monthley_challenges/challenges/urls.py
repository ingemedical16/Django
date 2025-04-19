from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:month>", views.monthley_challenges_by_number),
    path("<str:month>", views.monthly_challenges)
   
]