from django.shortcuts import render, redirect
from django.views import View
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

def thank_you(request):
    return render(request,"reviews/thank_you.html")
