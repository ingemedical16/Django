from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.urls import reverse
from django.template.loader import render_to_string

monthley_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn something new every week!",
    "april": "Drink at least 2 liters of water every day!",
    "may": "Practice meditation or mindfulness daily!",
    "june": "Read for at least 15 minutes every day!",
    "july": "Write down 3 things you're grateful for each day!",
    "august": "Try a new hobby or skill!",
    "september": "Limit screen time to 2 hours outside of work!",
    "october": "Avoid sugary snacks for the whole month!",
    "november": "Wake up before 7 AM every day!",
    "december": None
}
months = list(monthley_challenges.keys())

# Create your views here.

def index(request):
   return render(request, "challenges/index.html", {
       "months": months
   })
   

def monthley_challenge_by_number(request, month):
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
    
def monthly_challenge(request, month):
    try:
        challenge_text = monthley_challenges[month]
        return render(request,"challenges/challenge.html",{
            "text": challenge_text,
            "month": month,
            "back_link": reverse("index")
        })
      
    except:
       raise Http404()