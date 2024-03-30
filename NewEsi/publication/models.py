from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from rest_framework.authtoken.models import Token
import re

class UserManager(BaseUserManager):
    def create_user(self, email, **extra_fields):
        if email is None:
            raise TypeError('Users should have an email')
        user = self.model(email=self.normalize_email(email), is_staff=False, is_active=True, is_superuser=False, date_joined=timezone.now(), last_login=timezone.now(), **extra_fields)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        if email is None:
         raise TypeError('Superusers must have an email')
         if password is None:
            raise TypeError('Superusers must have a password')

        user = self.model(email=self.normalize_email(email), is_staff=True, is_active=True, is_superuser=True, date_joined=timezone.now(), **extra_fields)
        user.set_password(password)
        user.save()
        return user
class Laboratoire(models.Model):
    id_laboratoire = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    description = models.TextField()
    # # Chercheur=models.ManyToManyField('Chercheur', related_name='Labo_chercheur')
    # Partenaire=models.ManyToManyField(Partenaire_labo, related_name='Labo_partner')

    def __str__(self):
        return self.nom
class Equipe_Recherche(models.Model):
    id_equipe_recherche = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    laboratoire = models.ForeignKey(Laboratoire, related_name="Equipe_recherche", on_delete=models.CASCADE, default=None)
    theme=models.CharField(max_length=255, default='')
    def __str__(self):
        return self.nom
    
class Utilisateur(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, default="", unique=True)
    family_name = models.CharField(max_length=254, null=True, blank=True)
    first_name = models.CharField(max_length=254, null=True, blank=True)
    type = models.CharField(max_length=254, null=False, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(null=True, blank=True)
    is_chercheur=models.BooleanField(default=False)
    is_adminstrateur=models.BooleanField(default=False)
    is_editeur=models.BooleanField(default=False)
    is_responsable_fablab=models.BooleanField(default=False)
    is_directeur_relex=models.BooleanField(default=False)
    equipeRecherche = models.ForeignKey(Equipe_Recherche, related_name='chercheurs', on_delete=models.CASCADE, null=True, blank=True)

    contact = models.IntegerField(null=True, blank=True)
    objects = UserManager()  
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    def save(self, *args, **kwargs):
        # Check if the user is newly created
        if not self.pk:
            # Check if the email is valid
            is_valid_email = self.validate_email(self.email)
            if is_valid_email:
                # Create the user
                super().save(*args, **kwargs)
                # Generate the token
                token, _ = Token.objects.get_or_create(user=self)
                return token.key
            else:
                # Handle invalid email
                raise ValueError("Invalid email format")
        else:
            # For existing users, just save normally
            super().save(*args, **kwargs)
    @staticmethod
    def validate_email(email):
        # Check if email matches the pattern for esi.dz domain
        if re.match(r'^[a-zA-Z0-9._%+-]+@esi\.dz$', email):
            return True
        else:
            return False


# class ChercheurManager(models.Manager):
#     def get_queryset(self,*arg,**kwargs):
#         return super().get_queryset(*arg,**kwargs).filter(is_chercheur=True)




    

'''class Categorie(models.Model):
    id_categorie = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom'''


#club


class Club(models.Model):
    id_club=models.AutoField(primary_key=True)    
    nom = models.CharField(max_length=255)
    slogan= models.CharField(max_length=255)
    description= models.TextField()
    logo=models.ImageField(upload_to='club/', null=True, blank=True)
    def __str__(self):
        return self.nom
    

class MembreClub(models.Model):
    id_membre=models.AutoField(primary_key=True)    
    nom = models.CharField(max_length=255)
    prenom= models.CharField(max_length=255)
    post= models.TextField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='membres')

    def __str__(self):
        return self.nom     
    
#publications    
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
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='publications',null=True)

    def __str__(self):
        return self.titre

#recherche




class Partenaire_labo(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    contact = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=255)
    laboratoire = models.ForeignKey(Laboratoire, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


'''
class Chercheur(Utilisateur):
    
    equipe = models.ForeignKey(Equipe_Recherche, related_name='chercheurs', on_delete=models.CASCADE, default=None)
    def __str__(self):
        return f"{self.family_name} {self.first_name}"
'''
# class Chercheur(Utilisateur):
#     objects=ChercheurManager()
    
#     def save(self,*arg,**kwargs):
#         if not self.pk:
#             self.is_chercheur=True
#         return super().save(*arg,**kwargs)            

#     class Meta:
#         proxy = True

# class ChercheurEquipe(Chercheur):
#     equipe = models.ForeignKey(Equipe_Recherche, related_name='chercheurs', on_delete=models.CASCADE, default=None)
#     class Meta:
#         verbose_name = 'Chercheur'
#         verbose_name_plural = 'Chercheurs'

class Equipe_Projet(models.Model):
    id_equipe_projet = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    Chercheur=models.ManyToManyField('Utilisateur', related_name='equipe_projet')
    laboratoire = models.ForeignKey(Laboratoire, related_name="Equipes_projet", on_delete=models.CASCADE, default=None)
  
    def __str__(self):
        return self.nom
    
class Theme_Recherche(models.Model):
    id_theme = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=255)
    description = models.TextField()
    # projets=models.ManyToManyField(Projet,related_name= "themes")

    def __str__(self):
        return self.nom


class Projet(models.Model):
    id_projet = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=255)
    description = models.TextField()
    equipe_projet = models.ForeignKey(Equipe_Projet, on_delete=models.CASCADE)
    themes=models.ManyToManyField(Theme_Recherche,related_name= "themes")

    def __str__(self):
        return self.nom










        



#from here it should be in another app not in this one
    

class Demande_Partenariat(models.Model):
    nom = models.CharField(max_length=255)
    etat = models.CharField(max_length=50)
    contact = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.nom
    

class Devis(models.Model):
    etat = models.CharField(max_length=50 , default="en attente")
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





class Partenaire(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    contact = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=255)
    
    def __str__(self):
        return self.nom
    


