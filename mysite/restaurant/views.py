from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from restaurant.models import Restaurant, Faculty, RestaurantFood
from django.db.models import Q

# Create your views here.
def my_login(request):
    context = {
        'is_login': True
    }

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('index')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password!'
    return render(request, template_name='login.html', context=context)

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

    if request.method == 'POST':
        rating = request.POST.get('rating')
        res.rating += int(rating)
        res.count += 1
        res.save()
        print(rating)

    if res.count == 0:
        res.count = 1

    rating = res.rating / res.count
    # print(res)
    # print(menu)
    return render(request, 'detail.html', context={
        'restaurant': res,
        'menu': menu,
        'rating': rating
    })

def my_logout(request):
    logout(request)
    return redirect('index')