from django import forms
from .widgets import CustomClearableFileInput
from .models import Game, Competition, Chat, Club, Team


class FeesForm(forms.ModelForm):
    
    class Meta:
        model = Game
        fields = (
            'ref_trav',
            'asst1_trav',
            'asst2_trav',
        )


class CompetitionForm(forms.ModelForm):

    class Meta:
        model = Competition
        fields = ('comp',)


class ClubForm(forms.ModelForm):

    class Meta:
        model = Club
        fields = '__all__'

    club_badge = forms.ImageField(label="Club Badge", required=False,
                                  widget=CustomClearableFileInput)


class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = '__all__'

class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"


class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        widgets = {'date_time': DateTimeInput()}
        exclude = (
            'ref_total',
            'asst1_total',
            'asst2_total',
            'ref_trav',
            'asst1_trav',
            'asst2_trav',
        )

    


class ChatForm(forms.ModelForm):

    class Meta:
        model = Chat
        fields = '__all__'
