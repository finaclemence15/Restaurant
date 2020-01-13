from django.shortcuts import render
from django.http  import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    restaurant = Restaurant.objects.all()
    return render(request, 'index.html',{'restaurant':restaurant})

def search_locations(request):

    if 'location' in request.GET and request.GET["location"]:
        search_term = request.GET.get("location")
        searched_restaurant = Restaurant.search_by_location(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"searched_restaurant": searched_restaurant})

    else:
        message = "You haven't searched for any Location"
        return render(request, 'search.html',{"message":message})

def detail(request,image_id):
        image = Restaurant.objects.get(id = image_id)
        ratings = Rating.objects.all()
       
        return render(request,"details.html", {"image":image,"ratings":ratings})
    