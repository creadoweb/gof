from django import forms
from .models import EnregistrementVocal

class EnregistrementVocalForm(forms.ModelForm):
    class Meta:
        model = EnregistrementVocal
        fields = ['nom', 'fichier_audio']