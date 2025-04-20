from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    "december": "Perform one act of kindness each day!"
}

# Create your views here.

def index(request):
    return HttpResponse("this is working!")

def monthley_challenge_by_number(request, month):
    months = list(monthley_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
    
def monthly_challenge(request, month):
    try:
        challenge_text = monthley_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")