from django.http import HttpResponse
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)

from . import models
from . import forms

from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("guestbook:login")
    template_name = "registration/signup.html"


class MyLogoutView (LogoutView):
   pass


class MyLoginView(LoginView):
    template_name = "auth/login.html"
   # next_page = reverse_lazy("guestbook:list")

from django.contrib.auth.mixins import LoginRequiredMixin

class CommonViewSettings (LoginRequiredMixin):
    model = models.Entry
    form_class = forms.CreateEntryForm
    success_url = reverse_lazy("guestbook:list")

from django.contrib.auth.mixins import LoginRequiredMixin

class CreateEntryView(CommonViewSettings, CreateView):
    template_name = "guestbook/add.html"

    def form_valid(self, form):
       # if not self.request.user.is_authenticated:
        #    form.add_error(None, "Login first")

         #   return super(). form_invalid(form)
        
        if "shit" in form.data ["message"]:
            form.add_error("message","Bawal yan")
            form.instance.owner = self.request.user
        return super(). form_valid(form)

class UpdateEntryView(CommonViewSettings, UpdateView):
    template_name = "guestbook/update.html"

from django.http import Http404

class DeleteEntryView(DeleteView):
    model=models.Entry
    success_url = reverse_lazy("guestbook:list")
    template_name = "guestbook/delete.html"

    def get_object(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return None
        
        obj=None
        try:
            if self.request.user.is_superuser:
                obj = super().get_object(*args, **kwargs)
        except Http404:
            return None
        
        return obj

class EntryListView(ListView):
    template_name = "guestbook/index.html"
    model = models.Entry
    context_object_name = "entries"
    #queryset = models.Entry.objects.order_by("_datetime_created")


class EntryListView(ListView):
    template_name = "guestbook/index.html"
    model = models.Entry
    context_object_name = "entries"
#    pk_url_kwarg = "id"
    #queryset = models.Name.objects.filter(active=True)

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by("datetime_created")

        return qs
class MessageView(DetailView):
        template_name = "guestbook/message.html" 
        model = models.Entry
        pk_url_kward = "id"
#        if obj.first_name.upper().startswith("V"):
#            raise Http404
#        return obj
