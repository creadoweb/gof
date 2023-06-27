from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('enregistrement/', views.enregistrement_vocal_view, name='enregistrement_vocal'),
    path('liste_enregistrements/', views.liste_enregistrements, name='liste_enregistrements'),
]