from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view()), 
    path("raffle/random", views.RaffleView.as_view()), 
    path(
        "profile/<int:id>", 
        views.ProfileView.as_view(),
        name="profile"
    ),
]