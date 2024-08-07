from django import forms
from .models import Goal, GoalRating, FunctionalAreaRating

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title','description']

class GoalRatingForm(forms.ModelForm):
    class Meta:
        model = GoalRating
        fields = ['rating', 'comments']


class FunctionalAreaRatingForm(forms.ModelForm):
    class Meta:
        model = FunctionalAreaRating
        fields = ['rating','comments']