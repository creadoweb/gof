# Create your models here.
from django.db import models

class EnregistrementVocal(models.Model):
    nom = models.CharField(max_length=100)
    fichier_audio = models.FileField(upload_to='enregistrements')
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom