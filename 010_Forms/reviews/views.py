from django.shortcuts import render, redirect

from .forms import ReviewFrom
from .models import Review
# Create your views here.

def review(request):
    if request.method == 'POST':
       form = ReviewFrom(request.POST)
       if form.is_valid():
            review = Review(
                user_name = form.cleaned_data['user_name'], 
                review_text = form.cleaned_data['review_text'], 
                rating = form.cleaned_data['rating'])
            review.save()
            return redirect('thank_you')
    else:   
        form = ReviewFrom()
    
    return render(request,"reviews/review.html",{
        "form":form
    })

def thank_you(request):
    return render(request,"reviews/thank_you.html")
