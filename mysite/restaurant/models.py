from django.db import models
from food.models import Food


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    is_staff = models.BooleanField()
    is_superuser = models.BooleanField()


class Faculty(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='uploads/')
    open_time = models.TimeField(auto_now=False)
    close_time = models.TimeField(auto_now=False, null=False, default=0)
    rating = models.SmallIntegerField(default=0)
    approve_by = models.ForeignKey(User, on_delete=models.CASCADE)
    approve_date = models.DateField()

    def __str__(self):
        return '%s (%s)' % (self.name, self.owner)


class RestaurantFood(models.Model):
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)
    price = models.FloatField(default=0)

    def __str__(self):
        return '%s %s' % (self.food_id, self.price)
