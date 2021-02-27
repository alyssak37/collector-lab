from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User 

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

    toppings = models.ManyToManyField(Topping)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('icecreams_detail', kwargs={'icecream_id': self.id})

    def ate_for_today(self):
        return self.eating_set.filter(date=date.today()).count() >= len(MEALS)

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

class Photo(models.Model):
    url = models.CharField(max_length=200)
    icecream = models.ForeignKey(Icecream, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for icecream_id: {self.icecream_id} @{self.url}"