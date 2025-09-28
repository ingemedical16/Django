from django.shortcuts import render


# Create your views here.

def index(request):
    meetups =[
        {'title': 'A First Meetup', 'location': 'New York', 'slug': 'a-first-meetup'},
        {'title': 'A Second Meetup', 'location': 'New York', 'slug': 'a-second-meetup'},
        {'title': 'A Third Meetup', 'location': 'New York', 'slug': 'a-third-meetup'},  
    ]
    return render(request, 'meetups/index.html', {
        'meetups': meetups,
    })