from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Icecream, Topping

from .forms import EatingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def icecreams_index(request):
    icecreams = Icecream.objects.all()
    return render(request, 'icecreams/index.html', {'icecreams': icecreams})

def icecreams_detail(request, icecream_id):
    icecream = Icecream.objects.get(id=icecream_id)
    toppings_icecream_doesnt_have = Topping.objects.exclude(id__in = icecream.toppings.all().values_list('id'))
    eating_form = EatingForm
    return render(request, 
    'icecreams/detail.html', {
        'icecream': icecream,
        'eating_form': eating_form,
        'toppings': toppings_icecream_doesnt_have
    })

def add_eating(request, icecream_id):
    form = EatingForm(request.POST)
    if form.is_valid():
        new_eating = form.save(commit=False)
        new_eating.icecream_id = icecream_id
        new_eating.save()
    return redirect('icecreams_detail', icecream_id=icecream_id)

def assoc_topping(request, icecream_id, topping_id):
    Icecream.objects.get(id=icecream_id).toppings.add(topping_id)
    return redirect('icecreams_detail', icecream_id=icecream_id)

class IcecreamCreate(CreateView):
    model = Icecream
    fields = '__all__'

class IcecreamUpdate(UpdateView):
    model = Icecream
    fields = ['brand', 'description', 'calories']

class IcecreamDelete(DeleteView):
    model = Icecream
    success_url = '/icecreams/'

def toppings_index(request):
    toppings = Topping.objects.all()
    return render(request, 'toppings/index.html', {'toppings': toppings})

def toppings_detail(request, topping_id):
    topping = Topping.objects.get(id=topping_id)
    return render(request, 'toppings/detail.html', {'topping': topping})

class ToppingCreate(CreateView):
    model = Topping
    fields = '__all__'

class ToppingUpdate(UpdateView):
    model = Topping
    fields = ['name', 'color']

class ToppingDelete(DeleteView):
    model = Topping
    success_url = '/toppings/'