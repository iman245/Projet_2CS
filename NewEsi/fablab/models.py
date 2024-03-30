from django.db import models
from publication.models import Utilisateur
#to do for fablab






class DemandeMateriel(models.Model):
    id_demandeur=models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.TextField()
    Role = models.IntegerField(null=True, blank=True)
    etat = models.CharField(max_length=50)  # valide, en attente, rejeté
    responsable_fablab = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='material_requests')

    def __str__(self):
        return self.nom

#I thought of doing inheretence but I don't want to blender anything.
class PieceElect(models.Model):
    id_demandeur=models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.TextField()
    Role = models.IntegerField(null=True, blank=True)
    etat = models.CharField(max_length=50)  # valide, en attente, rejeté    
    demande_materiel = models.ForeignKey(DemandeMateriel, on_delete=models.CASCADE, related_name='electrical_pieces')

    def __str__(self):
        return self.nom