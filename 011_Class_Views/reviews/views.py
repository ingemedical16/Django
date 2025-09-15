from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .forms import ReviewFrom
from .models import Review

# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = ReviewFrom()

        return render(request,"reviews/review.html",{
        "form":form
    })

    def post(self, request):
        form = ReviewFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
        return render(request,"reviews/review.html",{
        "form":form
    })

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

class SingleReviewView(TemplateView):
    template_name = "reviews/single_review.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs.get("id")
        context["review"] = Review.objects.get(id=review_id)
        return context