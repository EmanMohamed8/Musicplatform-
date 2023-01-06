from django import forms
from .models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        name = self.cleaned_data.get("name")
        if len(name) > 50:
            raise forms.ValidationError("Please enter smaller name")
        return super().clean()
