from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
# Create your views here.

from main import models
from main import forms

def index(request):
    dict = {}
    return render(request,'main/index.html',context = dict)


def restaurants(request):

    query_set = models.Restaurant.objects.all()

    context ={"query_set": query_set}

    return render(request,'main/restaurants.html',context)

def add_restaurant(request):

    if request.method =="GET":
        form = forms.RestaurantForm()
    else:#POST request
        form = forms.RestaurantForm(request.POST)

        if form.is_valid():
            obj = form.save()
            return HttpResponse("Form added with id"+ str(obj.pk))

    context = {
    'form': form
    }
    return render(request,'main/addRestaurant.html',context)

def restaurant(request,id):

    # print(request.GET)
    #
    # try:
    #     r = request.GET['rating']
    #     s = request.GET['sorting']
    #     if(r==""):
    #         r = 0
    # except:
    #     r = 0
    #     s = "H2L"
    #
    # query_set = models.Restaurant.objects.all()
    # query_set = query_set.annotate(average_rating = Avg('review__rating')).filter(average_rating__gte = r)
    #
    # if(s=="L2H"):
    #     query_set=query_set.order_by('average_rating')
    # else:
    #     query_set=query_set.order_by('-average_rating')

    rest = get_object_or_404(models.Restaurant,pk=id)
    success = True

    #Handling the form

    if request.method == "GET":
        form = forms.ReviewForm()

    else:
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            obj = form.save(commit = False)
            obj.restaurant = rest
            obj.save()
            success = True
            form = forms.ReviewForm()

    context = { 'restaurant':rest,
                'form' : form,
                'success': success,
                }
    return render(request,'main/restaurant.html',context)

def review(request,id):
    obj = get_object_or_404(models.Review,pk=id)

    context ={
    'review':obj
    }
    return render(request,'main/review.html',context)
