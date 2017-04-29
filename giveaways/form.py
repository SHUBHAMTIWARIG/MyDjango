# from django.contrib.auth.forms import AuthenticationForm
from django import forms

from giveaways.models import Giveaway


class giveaway_form(forms.ModelForm):
    class Meta:
        model = Giveaway
        fields=[
            "giveaway_name",
            "description",
            "file",
            "screen_shot1",
            "screen_shot2",
            "screen_shot3",
            "website_link",
        ]

