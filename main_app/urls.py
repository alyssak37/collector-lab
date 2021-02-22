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
    path('icecreams/<int:icecream_id>/assoc_topping/<int:topping_id>/', views.assoc_topping, name='assoc_topping'),
    path('icecreams/<int:icecream_id>/add_photo/', views.add_photo, name='add_photo'),
    path('toppings/', views.toppings_index, name='topping_index'),
    path('toppings/<int:topping_id>/', views.toppings_detail, name='toppings_detail'),
    path('toppings/create', views.ToppingCreate.as_view(), name='toppings_create'),
    path('toppings/<int:pk>/update', views.ToppingUpdate.as_view(), name='toppings_update'),
    path('toppings/<int:pk>/delete', views.ToppingDelete.as_view(), name='toppings_delete'),
    path('accounts/signup/', views.signup, name='signup')
]

