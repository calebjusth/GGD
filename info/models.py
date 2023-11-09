from django.db import models

# Create your models here.


class About(models.Model):
    image = models.ImageField(default='')
    about_the_prophet = models.TextField()
    facebook_link = models.CharField(max_length=500, default='#')
    whats_app_link = models.CharField(max_length=500, default='#')
    instagram_link = models.CharField(max_length=500, default='#')
    twitter_link = models.CharField(max_length=500, default='#')
    youtube_link = models.CharField(max_length=500, default='#')

    def __str__(self):
        return self.about_the_prophet[:40]
    
class ChurchProgram(models.Model):
    image = models.ImageField(default='')
    service_day = models.CharField(max_length=50, default='')
    features = models.TextField()
    service_time = models.CharField(max_length=50, default='')
    def __str__(self):
        return self.service_day
    
class Charity(models.Model):
    image = models.ImageField(upload_to='charity', default='')
    title = models.CharField(max_length=50, default='')
    discription = models.TextField()
    def __str__(self):
        return self.title
    
class MembersList(models.Model):
    first_name = models.CharField(max_length=200, default='')
    last_name = models.CharField(max_length=200, default='')
    email = models.CharField(max_length=200, default='')
    phone = models.CharField(max_length=200, default='')
    country = models.CharField(max_length=200, default='')
    address = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.country
