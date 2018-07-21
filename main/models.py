from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.db.models import Avg
# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length = 100)
    address = models.TextField(max_length = 300)
    open_time = models.TimeField()
    close_time = models.TimeField()


    def get_data(self):
        return {
            'Name': self.name,
            'Address': self.address,
            'Open Time': self.open_time.strftime('%I:%M %p'),
            'Close Time': self.close_time.strftime('%I:%M %p'),
            'Average Rating': self.review_set.aggregate(models.Avg('rating'))['rating__avg'],
    }


    def get_rating(self):
        return self.review_set.aggregate(Avg('rating'))['rating__avg']


    def __str__(self):
        return self.name

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete = models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.CharField(max_length = 100)
    title= models.CharField(max_length=1024)
    rating  = models.IntegerField(validators = [MaxValueValidator(5),MinValueValidator(0)])

    def get_stars(self):
        return "* "*self.rating

    def __str__(self):
        return self.title
