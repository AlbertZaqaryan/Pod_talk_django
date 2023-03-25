from django import forms
from .models import Lastest_Episode


class EpisodeForm(forms.ModelForm):
    class Meta:
        model = Lastest_Episode
        fields = ['button1', 'button2', 'button3', 'button4']