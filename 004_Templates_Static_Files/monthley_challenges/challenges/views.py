from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    "december": "Perform one act of kindness each day!"
}
months = list(monthley_challenges.keys())

# Create your views here.

def index(request):
    list_items = ""
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)
   

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
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")