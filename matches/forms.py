from django import forms
from django.core.validators import RegexValidator
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

    comp = forms.CharField(validators=[RegexValidator(r'^[a-zA-Z]+( \w+)*$',
                           message="Competition name must contain \
                               words and numbers")])


class ClubForm(forms.ModelForm):
    """ A form to allow superusers to add and edit clubs """
    class Meta:
        model = Club
        fields = '__all__'

    club_name = forms.CharField(validators=[RegexValidator(
                                r'^[a-zA-Z]+( \w+)*$',
                                message="Club name must contain \
                                    words and numbers")])
    club_badge = forms.ImageField(label="Club Badge", required=False,
                                  widget=CustomClearableFileInput)


class TeamForm(forms.ModelForm):
    """ A form to allow superusers to add and editteams """
    class Meta:
        model = Team
        fields = '__all__'

    team_name = forms.CharField(validators=[RegexValidator(
                                r'^[a-zA-Z]+( \w+)*$',
                                message="Team name must contain \
                                    words and numbers")])
    short_name = forms.CharField(label='Short Team name',
                                 validators=[RegexValidator(
                                    r'^[a-zA-Z]+( \w+)*$',
                                    message="Team short name must contain \
                                    words and numbers")])
    manager_coach = forms.CharField(label='Manager/Coach',
                                    validators=[RegexValidator(
                                        r'^[a-zA-Z]+( \w+)*$',
                                        message="Manager/Coach name must contain \
                                            words and numbers")])


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

    # chained dropdown elements adapted from
    # https://simpleisbetterthancomplex.com/tutorial/2018/01/29/
    # how-to-implement-dependent-or-chained-dropdown-list-with-django.html

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['home_team'].queryset = Team.objects.none()
        self.fields['away_team'].queryset = Team.objects.none()

        if 'age' in self.data:
            try:
                age_id = int(self.data.get('age'))
                self.fields['home_team'].queryset = Team.objects.filter(
                    age_id=age_id).order_by('team_name')
                self.fields['away_team'].queryset = Team.objects.filter(
                    age_id=age_id).order_by('team_name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            age_id = self.instance.age.pk
            self.fields['home_team'].queryset = Team.objects.filter(
                team_name__contains=self.instance.age).order_by('team_name')
            self.fields['away_team'].queryset = Team.objects.filter(
                team_name__contains=self.instance.age).order_by('team_name')


class ChatForm(forms.ModelForm):
    """ Form to allow  Coaches and Referees to post messages per game """
    class Meta:
        model = Chat
        fields = '__all__'

    image = forms.ImageField(label="Message Image", required=False,
                             widget=CustomClearableFileInput)
