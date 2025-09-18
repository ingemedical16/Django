from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, FormView
from .forms import ReviewFrom
from .models import Review

# Create your views here.

class ReviewView(CreateView):
    model = Review
    form_class = ReviewFrom
    template_name = "reviews/review.html"
    success_url = "/thank-you"
    
    
   

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Your review has been submitted successfully."
        return context


class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    #context_object_name = "review"
    #pk_url_kwarg = "id"
    
