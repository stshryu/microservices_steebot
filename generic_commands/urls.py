from django.urls import path
from generic_commands import views

urlpatterns = [
    path('roll/', views.diceroll),
    path('flip/', views.coinflip),
]