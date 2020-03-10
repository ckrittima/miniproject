from webbrowser import register

from django.contrib import admin

from .models import Food, Restaurant, User, Faculty, RestaurantFood

# Register your models here.
admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(Faculty)
admin.site.register(Food)
admin.site.register(RestaurantFood)
