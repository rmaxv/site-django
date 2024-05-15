from django.contrib import admin

from .models import Trip
from .models import Passenger_detail
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'location', 'interests', 'about_me', 'img3')


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('destination', 'start_date', 'end_date', 'desc')


@admin.register(Passenger_detail)
class Passenger_detailAdmin(admin.ModelAdmin):
    list_display = ('Trip_id', 'start_date', 'end_date', 'username', 'city', 'interests', 'about_me')

