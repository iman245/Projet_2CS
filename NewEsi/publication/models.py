from django.db import models
from django.contrib.auth.models import Permission,AbstractUser





class DemandePublication(models.Model):
    id_publication = models.IntegerField(primary_key=True)
    titre = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='publications/', null=True, blank=True)
    etat = models.CharField(max_length=50)  # valide, en attente, rejeté
    date_debut = models.DateTimeField(null=True, blank=True)
    date_fin = models.DateTimeField(null=True, blank=True)
    date_publication = models.DateTimeField(null=True, blank=True)
    is_event=models.BooleanField(default=False)
    is_actualite=models.BooleanField(default=False)
    is_article=models.BooleanField(default=False)  
    category=models.CharField(max_length=255)#I don't know exactly what to put here at this moment, I will change it later
    #Note if you want to customize event,actualite or anything you should make a proxy model for that thing. 
    #like chercheur for Utilisateur

    
    def __str__(self):
        return self.titre
















#Pretty much useless now since I am going to do auth using proxy models.
#All user types are in User application.




"""class Utilisateur(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    contact = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=255)
    mot_de_passe = models.CharField(max_length=255)
    type = models.CharField(max_length=50)#editeur,admin,club....
    def __str__(self):
        return self.nom
'''lass Utilisateur(AbstractUser):
    contact = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.nom'''





#class Chercheur(Utilisateur):
    #link to a lab
 #   pass

'''class Categorie(models.Model):
    id_categorie = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom'''

class Publication(models.Model):
    id_publication = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='publications/', null=True, blank=True)
    etat = models.CharField(max_length=50)  # valide, en attente, rejeté
    type_publication = models.CharField(max_length=50)  # event/actualité/article
    date_debut = models.DateTimeField(null=True, blank=True)
    date_fin = models.DateTimeField(null=True, blank=True)
    date_publication = models.DateTimeField(null=True, blank=True)
    #category = models.ForeignKey(Categorie, on_delete=models.CASCADE)#if category gets deleted all post gets deleted 
    #I don't think it should be a class by it's own if we won't change the class frequently
    category=models.CharField(max_length=50)
    def __str__(self):
        return self.titre



class Equipe_Projet(models.Model):
    id_equipe_projet = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=255)
    Chercheur=models.ManyToManyField('Chercheur', related_name='equipes_projet')
    def __str__(self):
        return self.nom
    
class Projet(models.Model):
    id_projet = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=255)
    description = models.TextField()
    equipe_projet = models.ForeignKey(Equipe_Projet, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Equipe_Recherche(models.Model):
    id_equipe_recherche = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nom
class Theme_Recherche(models.Model):
    id_theme = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=255)
    description = models.TextField()
    Equipe_Recherche = models.ForeignKey(Equipe_Recherche, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

        



#from here it should be in another app not in this one
    

class Demande_Partenariat(models.Model):
    id_partenariat = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=255)
    etat = models.CharField(max_length=50)
    contact = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=255)
    def __str__(self):
        return self.nom
    

class Devis(models.Model):
    id_devis = models.IntegerField(primary_key=True)
    etat = models.CharField(max_length=50)
    montant = models.FloatField(null=True, blank=True) 
    def __str__(self):
        return self.montant

class Formation(models.Model):
    id_formation = models.IntegerField(primary_key=True)
    titre = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=50) #a la carte/avant promo
    prix = models.FloatField(null=True, blank=True) 
    def __str__(self):
        return self.titre



class Laboratoire(models.Model):
    id_laboratoire = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=255)
    description = models.TextField()
    Chercheur=models.ManyToManyField('Chercheur', related_name='Labo_chercheur')
    Partenaire=models.ManyToManyField('Partenaire', related_name='Labo_chercheur')
    def __str__(self):
        return self.nom

class Partenaire(models.Model):
    id_partenaire = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=255)
    description = models.TextField()
    contact = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=255)
    def __str__(self):
        return self.nom
"""