from django import forms

from main import models

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = models.Restaurant
        fields = "__all__"

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        exclude = ['restaurant',]
