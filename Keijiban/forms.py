from django import forms
from .models import Hitokoto


class HitokotoForm(forms.ModelForm):
    class Meta:
        model = Hitokoto
        fields = ('name', 'comment')
