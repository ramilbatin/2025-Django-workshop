from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView

from . import models
import random

from django.shortcuts import get_object_or_404
from django.http import Http404

class ProfileView(DetailView):
    template_name = "names/profile.html"
    model = models.Name
    context_object_name="person"
    pk_url_kwarg = "id"
    #queryset = models.Name.objects.filter(active=True)

def get_object (self):
    obj = super().get_object()
    if obj.first_name.upper(). startswith("V"):
        raise Http404
    return obj


class RaffleView(TemplateView):
    template_name = "names/raffle.html"
    model = models.Name
    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        objs = models.Name.objects.filter(active=True).all()
        #objs = list(models.Name.objects.all())
        if objs.count():
            winner = random.choice(objs)
        else:
            winner = None
        #winner = random.choice(objs)
        context['winner'] = winner
        return context
    
class HomeView(ListView):
    template_name = "names/index.html"
    model = models.Name
    