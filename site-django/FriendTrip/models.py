from django.db import models


class Trip(models.Model):
    id = models.IntegerField(primary_key=True)
    destination = models.CharField(max_length=70)
    img1 = models.ImageField(upload_to='pics')
    img2 = models.ImageField(upload_to='pics')
    number = models.IntegerField(default=2)
    start_date = models.DateField()
    end_date = models.DateField()
    rating = models.IntegerField(default=5)
    dest_name = models.CharField(max_length=25)
    desc = models.TextField()


class Passenger_detail(models.Model):
    Trip_id = models.AutoField(primary_key=True)
    Trip_same_id = models.IntegerField(default=1)
    first_name = models.CharField(max_length=15)
    age = models.IntegerField()
    username = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    city = models.CharField(max_length=20)
    interests = models.TextField()
    about_me = models.TextField()


class Profile(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    location = models.CharField(max_length=255)
    interests = models.TextField()
    about_me = models.TextField()
    img3 = models.ImageField(upload_to='pics')







