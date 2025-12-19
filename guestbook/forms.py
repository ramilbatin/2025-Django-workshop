from django import forms

from . import models

class CreateEntryForm(forms.ModelForm):
    class Meta:
        model = models.Entry
#        fields = "__all__"
#        exclude = ("datetime_created",)

        fields = ("message",)

    