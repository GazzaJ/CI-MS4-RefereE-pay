from django import forms
from .widgets import CustomClearableFileInput, CustomDateTimeInput
from .models import Game, Competition, Chat, Club, Team


class FeesForm(forms.ModelForm):
    """ A form to allow superusers and refs to add travel expenses """
    class Meta:
        model = Game
        fields = (
            'ref_trav',
            'asst1_trav',
            'asst2_trav',
        )


class CompetitionForm(forms.ModelForm):
    """ A form to allow superusers to add competitions """
    class Meta:
        model = Competition
        fields = ('comp',)


class ClubForm(forms.ModelForm):
    """ A form to allow superusers to add and edit clubs """
    class Meta:
        model = Club
        fields = '__all__'

    club_badge = forms.ImageField(label="Club Badge", required=False,
                                  widget=CustomClearableFileInput)


class TeamForm(forms.ModelForm):
    """ A form to allow superusers to add and editteams """
    class Meta:
        model = Team
        fields = '__all__'


class GameForm(forms.ModelForm):
    """ A form to allow superusers to add and edit matches """
    class Meta:
        model = Game
        fields = (
            'age',
            'competition',
            'home_team',
            'away_team',
            'date_time',
            'venue',
            'referee',
            'asst_referee1',
            'asst_referee2',
        )

    date_time = forms.DateTimeField(label="KO Date & Time", required=True,
                                    widget=CustomDateTimeInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['home_team'].queryset = Team.objects.none()
        #self.fields['away_team'].queryset = Team.objects.none()


class ChatForm(forms.ModelForm):
    """ Form to allow  Coaches and Referees to post messages per game """
    class Meta:
        model = Chat
        fields = '__all__'
