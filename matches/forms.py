from django import forms
from .models import Game


class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields[]
