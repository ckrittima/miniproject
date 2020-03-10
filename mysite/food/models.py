from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=500)
    is_vegan = models.BooleanField(default=False)

    def __str__(self):
        return self.name