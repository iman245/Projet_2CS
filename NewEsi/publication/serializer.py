# serializers.py
from rest_framework import serializers
from .models import Utilisateur,Publication

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ['nom', 'contact', 'email', 'mot_de_passe', 'type'] #exculuding Id since it's auto increment
class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'