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
def meetup_details(request, meetup_slug): 
    slected_meetup = {
        'title': 'A First Meetup',
        'description': 'This is a first meetup description',
    }   
    return render(request, 'meetups/meetup_details.html', {
        'meetup_title': slected_meetup['title'],
        'meetup_description': slected_meetup['description'],
    })