import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Icecream, Topping, Photo

from .forms import EatingForm

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'alyssa-nexus-catcollector'
# Create your views here.
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('icecreams_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def icecreams_index(request):
    icecreams = Icecream.objects.filter(user=request.user)
    return render(request, 'icecreams/index.html', {'icecreams': icecreams})

@login_required
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

@login_required
def add_eating(request, icecream_id):
    form = EatingForm(request.POST)
    if form.is_valid():
        new_eating = form.save(commit=False)
        new_eating.icecream_id = icecream_id
        new_eating.save()
    return redirect('icecreams_detail', icecream_id=icecream_id)

@login_required
def assoc_topping(request, icecream_id, topping_id):
    Icecream.objects.get(id=icecream_id).toppings.add(topping_id)
    return redirect('icecreams_detail', icecream_id=icecream_id)

@login_required
def add_photo(request, icecream_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, icecream_id=icecream_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('icecreams_detail', icecream_id=icecream_id)

class IcecreamCreate(LoginRequiredMixin, CreateView):
    model = Icecream
    fields = ['name', 'brand', 'description', 'calories']

class IcecreamUpdate(LoginRequiredMixin, UpdateView):
    model = Icecream
    fields = ['brand', 'description', 'calories']

class IcecreamDelete(LoginRequiredMixin, DeleteView):
    model = Icecream
    success_url = '/icecreams/'

def toppings_index(request):
    toppings = Topping.objects.all()
    return render(request, 'toppings/index.html', {'toppings': toppings})

def toppings_detail(request, topping_id):
    topping = Topping.objects.get(id=topping_id)
    return render(request, 'toppings/detail.html', {'topping': topping})

class ToppingCreate(LoginRequiredMixin, CreateView):
    model = Topping
    fields = '__all__'

class ToppingUpdate(LoginRequiredMixin, UpdateView):
    model = Topping
    fields = ['name', 'color']

class ToppingDelete(LoginRequiredMixin, DeleteView):
    model = Topping
    success_url = '/toppings/'