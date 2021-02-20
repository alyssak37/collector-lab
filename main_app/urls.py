from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('icecreams/', views.icecreams_index, name='icecream_index'),
    path('icecreams/<int:icecream_id>/', views.icecreams_detail, name='icecreams_detail'),
    path('icecreams/create', views.IcecreamCreate.as_view(), name='icecreams_create'),
    path('icecreams/<int:pk>/update', views.IcecreamUpdate.as_view(), name='icecreams_update'),
    path('icecreams/<int:pk>/delete', views.IcecreamDelete.as_view(), name='icecreams_delete'),
    path('icecreams/<int:icecream_id>/add_eating/', views.add_eating, name='add_eating'),
    path('toppings/', views.toppings_index, name='topping_index'),
    path('toppings/<int:topping_id>/', view.toppings_detail, name='toppings_detail'),
    
]

