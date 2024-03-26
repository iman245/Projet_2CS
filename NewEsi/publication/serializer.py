# serializers.py
from rest_framework import serializers
from .models import Utilisateur,Publication , Token

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