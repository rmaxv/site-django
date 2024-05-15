from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('create_trip/logout', views.logout, name='logout'),
    path('search', views.search, name='search'),
    path('create_trip', views.create_trip, name='create_trip'),
    path('search_trip', views.all_trips, name='search_trip'),
]
