from django import forms
from movies.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['movie', 'name','rating']
        widgets = {
            'movie': forms.HiddenInput(),
            'name': forms.Textarea(attrs={'rows': 2}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            
        }