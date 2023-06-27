

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EnregistrementVocalForm
from .models import EnregistrementVocal
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

def index(request):
    return render(request, 'polls/accueil.html')
@csrf_exempt
def enregistrement_vocal_view(request):
    if request.method == 'POST':
        form = EnregistrementVocalForm(request.POST, request.FILES)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            
            # Get the uploaded file from the request.FILES dictionary
            fichier_audio = request.FILES['fichier_audio']
            
            # Create a new instance of EnregistrementVocal model
            enregistrement = EnregistrementVocal(nom=nom, fichier_audio=fichier_audio)
            enregistrement.save()
            messages.success(request, 'Enregistrement vocal ajouté avec succès.')
            # Perform any necessary actions or redirections
            
            return redirect('enregistrement_vocal')
    
    else:
        form = EnregistrementVocalForm()
    
    return render(request, 'polls/enregistrement_vocal.html', {'form': form})




def liste_enregistrements(request):
    enregistrements = EnregistrementVocal.objects.all()
    return render(request, 'polls/liste_enregistrements.html', {'enregistrements': enregistrements})
