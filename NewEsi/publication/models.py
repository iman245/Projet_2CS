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


class Chercheur(Utilisateur):
    #link to a lab
    pass

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
