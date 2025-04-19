from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

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
    return HttpResponse(month)
    
def monthly_challenge(request, month):
    try:
        challenge_text = monthley_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")