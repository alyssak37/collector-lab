from django.db import models
from django.urls import reverse 

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

# Create your models here.
class Topping(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toppings_detail', kwargs={'topping_id': self.id})

class Icecream(models.Model):
    name = models.CharField(max_length=250)
    brand = models.CharField(max_length=250)
    description = models.TextField(max_length=250)
    calories = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('icecreams_detail', kwargs={'icecream_id': self.id})

class Eating(models.Model):
    date = models.DateField('eating date')
    meal = models.CharField(
        max_length=1, 
        choices=MEALS,
        default=MEALS[0][0]
    )

    icecream = models.ForeignKey(Icecream, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} at {self.date}"

    class Meta:
        ordering = ['-date']

