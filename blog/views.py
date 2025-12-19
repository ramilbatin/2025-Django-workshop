from django.http import HttpResponse
from django.views.generic import TemplateView

from . import models


class HomeView(TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["posts"] = models.Post.objects.filter(active=True).all()
        return context


class HomeView2(TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["posts"] = [
            {
                "title": "First post!",
                "post": "This is my first <b>blog post</b>!",
            }
        ]
        return context