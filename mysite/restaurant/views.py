from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from restaurant.models import Restaurant, Faculty, RestaurantFood


# Create your views here.
def index(request):
    faculty = Faculty.objects.all()
    restaurant = {}
    for item in faculty:
        res = Restaurant.objects.filter(faculty_id=item.id)
        restaurant[item.id] = {'name': item.name, 'res': res}
    # print(restaurant)
    return render(request, 'index.html', context={
        'restaurant': restaurant
    })


def detail(request, restaurant_id):
    search = request.GET.get('search', '')
    res = Restaurant.objects.get(id=restaurant_id)
    menu = RestaurantFood.objects.filter(restaurant_id=restaurant_id)
    # print(res)
    # print(menu)
    return render(request, 'detail.html', context={
        'restaurant': res,
        'menu': menu,

    })
