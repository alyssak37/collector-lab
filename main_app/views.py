from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Icecream

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
    eating_form = EatingForm
    return render(request, 
    'icecreams/detail.html', {
        'icecream': icecream,
        'eating_form': eating_form
    })

def add_eating(request, icecream_id):
    form = EatingForm(request.POST)
    if form.is_valid():
        new_eating = form.save(commit=False)
        new_eating.icecream_id = icecream_id
        new_eating.save()
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

def toppings_detail(request):
    topping =  Topping.objects.get(id=icecream_id)
    return render(request, 'toppings/detail.html', {'topping': topping})