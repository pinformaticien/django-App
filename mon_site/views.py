from django.shortcuts import render

import requests, json

from .models import Contact

# Create your views here.

def index(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        

        r = requests.get('http://api.icndb.com/jokes/random?firstName='+firstname+'&lastName='+lastname)
        json_data = json.loads(r.text)

        joke = json_data.get('value').get('joke')
        
        context = {'joker':joke}

        return render(request, 'mon_site/index.html', context)
    else:
        firstname = 'Sanoussy'
        lastname = 'Gassama'
        

        r = requests.get('http://api.icndb.com/jokes/random?firstName='+firstname+'&lastName='+lastname)
        json_data = json.loads(r.text)

        joke = json_data.get('value').get('joke')
        
        context = {'joker':joke}

        return render(request, 'mon_site/index.html', context)

def portfolio(request):
    return render(request, 'mon_site/portfolio.html')

def contact(request):
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')
        
        c = Contact(email=email_r, subject=subject_r, message=message_r)
        c.save()

        return render(request, 'mon_site/thank.html')
    else:
        return render(request, 'mon_site/contact.html')