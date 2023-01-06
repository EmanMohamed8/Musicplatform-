from django import forms
from .models import Artist
from django.core.exceptions import ValidationError


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = {
            'stageName',
            'socialLink',
        }

    def clean(self):
        cleaned_data = super().clean()
        stageName = cleaned_data.get("stageName")
        if Artist.objects.filter(stageName__iexact=stageName).exists():
            print('azay')
            raise forms.ValidationError("This stageName is already exist")
        return super().clean()
