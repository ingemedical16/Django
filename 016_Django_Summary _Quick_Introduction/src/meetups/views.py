from django.shortcuts import render, redirect

from .models import Meetup, Participant
from .forms import RegistrationForm
# Create your views here.

def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', {
        'meetups': meetups,
    })
def meetup_details(request, meetup_slug): 
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
            
        else:
             registration_form = RegistrationForm(request.POST)
             if registration_form.is_valid():
                email = registration_form.cleaned_data['email']
                name = registration_form.cleaned_data['name']

                 # Vérifier si le participant existe déjà
                participant, _ = Participant.objects.get_or_create(
                    email=email,
                    defaults={'name': name}
                )


                # Lier le participant au meetup
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration')

        return render(request, 'meetups/meetup-details.html', {
                'meetup': selected_meetup,
                'form':registration_form
            })
    except Exception as e:
        print(e)
        return render(request, 'meetups/meetup-details.html', {
            'meetup': None,
            'title': 'Meetup Not Found',
        }) 

def confirm_registration(request):
    return render(request,'meetups/registration-success.html') 