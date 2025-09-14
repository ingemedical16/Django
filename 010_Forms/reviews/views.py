from django.shortcuts import render, redirect

from .forms import ReviewFrom
# Create your views here.

def review(request):
    if request.method == 'POST':
       form = ReviewFrom(request.POST)
       if form.is_valid():
            print(form.cleaned_data)
            return redirect('thank_you')
       
    form = ReviewFrom()
    
    return render(request,"reviews/review.html",{
        "form":form
    })

def thank_you(request):
    return render(request,"reviews/thank_you.html")
