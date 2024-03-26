from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.
class Utilisateur(AbstractUser):
    is_chercheur=models.BooleanField(default=False)
    is_adminstrateur=models.BooleanField(default=False)
    is_editeur=models.BooleanField(default=False)
    is_responsable_fablab=models.BooleanField(default=False)
    is_directeur_relex=models.BooleanField(default=False)

    contact = models.IntegerField(null=True, blank=True)
  
class ChercheurManager(models.Manager):
    def get_queryset(self,*arg,**kwargs):
        return super().get_queryset(*arg,**kwargs).filter(type=Utilisateur.Types.CHERCHEUR)

class Chercheur(Utilisateur):
    objects=ChercheurManager()
        
    def save(self,*arg,**kwargs):
        if not self.pk:
            self.type=Utilisateur.Types.CHERCHEUR
        return super().save(*arg,**kwargs)            

    class Meta:
        proxy = True




    


