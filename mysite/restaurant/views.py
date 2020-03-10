from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from restaurant.models import Restaurant, Faculty


# Create your views here.
def index(request):
    faculty = Faculty.objects.all()
    restaurant = {}
    for item in faculty:
        res = Restaurant.objects.filter(faculty_id=item.id)
        restaurant[item.id] = {'name': item.name, 'res': res}
    print(restaurant)
    return render(request, 'index.html', context={
        'restaurant': restaurant
    })


def detail(request):
    faculty = Faculty.objects.all()
    print(faculty)
    return render(request, 'detail.html', context={
        'faculty': faculty
    })
