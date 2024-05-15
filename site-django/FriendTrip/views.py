from datetime import datetime

from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import *
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.forms.formsets import formset_factory
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Trip
from .models import Passenger_detail
from .models import Profile


# Create your views here.
def index(request):
    dests = Trip()
    dest1 = []
    return render(request, 'index.html', {'dests': dests, 'dest1': dest1})


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(password=password1, email=email, last_name=last_name,
                                                first_name=first_name)
                user.save()
                print('user Created')
                return redirect('login')
        else:
            messages.info(request, 'Password is not matching ')
            return redirect('register')
    else:
        return render(request, 'register.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, 'Successfully Logged in')
            email = request.user.email
            print(email)
            content = 'Hello ' + request.user.first_name + ' ' + request.user.last_name + '\n' + 'You are logged in in our site.keep connected and keep travelling.'
            return redirect('index')
        else:
            messages.info(request, 'Invalid credential')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


@login_required(login_url='login')
def create_trip(request):
    if request.method == 'POST':
        title = request.POST['title']
        destination = request.POST['destination']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        description = request.POST['description']

        trip = Trip(
            title=title,
            destination=destination,
            start_date=start_date,
            end_date=end_date,
            description=description,
            creator=Profile(user=request.user)
        )

        return redirect('index')
    else:
        return render(request, 'create_trip.html')

def all_trips(request):
    trips = Trip.objects.all()
    return render(request, 'search_trip.html', {'trips': trips})

def search(request):
    if request.method == 'GET':
        destination = request.GET.get('destination')
        date = request.GET.get('start_date')
        trips = Trip.objects.filter(destination=destination, start_date=date)
        return render(request, 'search_trip.html', {'trips': trips})
    else:
        return render(request, 'search_trip.html')


class KeyValueForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField()


def Passenger_detail_def(request, destination):
    KeyValueFormSet = formset_factory(KeyValueForm, extra=1)
    if request.method == 'POST':
        formset = KeyValueFormSet(request.POST)
        if formset.is_valid():
            temp_date = datetime.strptime(request.POST['start_date'], "%Y-%m-%d").date()
            date1 = datetime.now().date()
            if temp_date < date1:
                return redirect('index')
            obj = Passenger_detail(Trip_id=3)
            pipo_id = obj.Trip_same_id
            #pipo_id =4
            print(request.POST['start_date'])
            #temp_date = parse_date(request.POST['trip_date'])
            temp_date = datetime.strptime(request.POST['start_date'], "%Y-%m-%d").date()
            usernameget = request.user.get_username()
            print(temp_date)
            obj.Trip_same_id = (pipo_id + 1)
            obj.save()
            return render(request, 'create_trip.html', {'destination': destination})
    else:
        formset = KeyValueFormSet()

        return render(request, 'create_trip.html', {'formset': formset, 'destination': destination})

