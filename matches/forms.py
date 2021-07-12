from django import forms
from .models import Game


class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        matches = Game.objects.all()

        self.fields['home_team'].choices
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-3'

