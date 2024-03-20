from django.db import models

class Utilisateur(models.Model):
    id_utilisateur = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=255)
    contact = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=255)
    mot_de_passe = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class Categorie(models.Model):
    id_categorie = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class DemandePublication(models.Model):
    id_publication = models.IntegerField(primary_key=True)
    titre = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='publications/', null=True, blank=True)
    etat = models.CharField(max_length=50)  # valide, en attente, rejeté
    type_publication = models.CharField(max_length=50)  # event/actualité
    date_debut = models.DateTimeField(null=True, blank=True)
    date_fin = models.DateTimeField(null=True, blank=True)
    date_publication = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.titre

class Publication(models.Model):
    id_categorie = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom
