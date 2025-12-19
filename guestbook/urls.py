from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

app_name = "guestbook"


urlpatterns = [
    path("", views.EntryListView.as_view(), name="list"),
    path("add", views.CreateEntryView.as_view(),
         name="add"),
    path("update/<int:pk>", views.UpdateEntryView.as_view(),
         name="update"),
     path("delete/<int:pk>", views.DeleteEntryView.as_view(),
         name="delete"),

    path("login", views.MyLoginView.as_view(),
        name="login"),
    path("logout", LogoutView.as_view(),
        name="logout"),

    path("signup", views.SignupView.as_view(),
        name="signup"),
]