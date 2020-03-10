from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from restaurant.models import Restaurant, Faculty, RestaurantFood

from django.db.models import Q


# Create your views here.
def index(request):
    context = {
        'restaurant': {},
        'search': [],
        'search_text': ""
    }

    if request.method == 'POST':
        search = request.POST.get('search', '')
        s_res = Restaurant.objects.filter(Q(name__icontains=search))
        context['search'] = s_res
        context['search_text'] = search
    else:
        faculty = Faculty.objects.all()
        restaurant = {}
        for item in faculty:
            res = Restaurant.objects.filter(faculty_id=item.id)
            restaurant[item.id] = {'name': item.name, 'res': res}
            context['restaurant'] = restaurant

    return render(request, 'index.html', context=context)


def detail(request, restaurant_id):
    res = Restaurant.objects.get(id=restaurant_id)
    menu = RestaurantFood.objects.filter(restaurant_id=restaurant_id)
    # print(res)
    # print(menu)
    return render(request, 'detail.html', context={
        'restaurant': res,
        'menu': menu,

    })
