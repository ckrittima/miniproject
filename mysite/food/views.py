from django.shortcuts import render
from food.models import Food
from restaurant.models import RestaurantFood

# Create your views here.
def detail(request):
    food = Food.objects.all()
    print(food)
    
    return render(request, 'detail.html', context={
        'food': food
    })