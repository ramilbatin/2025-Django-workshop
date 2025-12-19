from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/exercise2
    path("exercise1", views.HomeView2.as_view()), 
    path("exercise2", views.HomeView.as_view()),
]