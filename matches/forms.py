from django import forms
from .models import Game, Competition, Chat


class CompetitionForm(forms.ModelForm):
    comp = forms.CharField(max_length=100, label='Competition',
                           empty_value=None)

    class Meta:
        model = Competition
        fields = ('comp',)


class GameForm(forms.ModelForm):

    class Meta:        
        model = Game
        exclude = (
            'ref_total',
            'asst1_total',
            'asst2_total',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        placeholders = {
            'age': 'Age Group',
            'competition': 'Competition',
            'home_team': 'Home Team',
            'away_team': 'Away Team',
            'date_time': 'KO Date & Time',
            'venue': 'Match Venue',
            'referee': 'Referee',
            'asst_referee1': 'Assistant Referee #1',
            'asst_referee2': 'Assistant Referee #2',
        }

        self.fields['home_team'].choices
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-3'

        # for field in self.fields:            
        #     if self.fields[field].required:
        #         placeholder = f'{placeholders[field]} *'
        #     else:
        #         placeholder = placeholders[field]
        #         self.fields[field].widget.attrs['placeholder'] = placeholder
        # self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
        # self.fields[field].label = False


class ChatForm(forms.ModelForm):

    class Meta:
        model = Chat
        fields = '__all__'
