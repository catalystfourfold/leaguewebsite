from django import forms
from .models import Division, Team, Player, Game

class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = ['name']

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'division']

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'team']

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['date', 'day', 'time', 'status', 'score', 'visitors', 'home', 'venue']

    def __init__(self, division_id, *args, **kwargs):
        super(GameForm, self).__init__(*args, **kwargs)

        # Filter visitors and home fields based on division_id
        self.fields['visitors'].queryset = Team.objects.filter(division=division_id)
        self.fields['home'].queryset = Team.objects.filter(division=division_id)