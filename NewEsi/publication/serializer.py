# serializers.py
from rest_framework import serializers
from .models import Utilisateur,Publication , Token ,  Partenaire , Demande_Partenariat, Devis

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ['id', 'email', 'family_name', 'first_name', 'is_active', 'date_joined', 'last_login']
class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'


class tokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key']
        

class PartenaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partenaire
        fields = '__all__'



class DemandePartenariatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demande_Partenariat
        fields = '__all__'  # Sérialiser tous les champs du modèle

class DevisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devis
        fields = '__all__'  # Sérialiser tous les champs du modèle