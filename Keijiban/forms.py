from django import forms
from .models import Hitokoto


class HitokotoForm(forms.Form):
    class Meta:
        model = Hitokoto
        exclude = ('created_at',)
