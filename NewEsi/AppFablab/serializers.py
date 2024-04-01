from rest_framework import serializers
from .models import Piece, DemandeMateriel, FablabInscriptionUtilisateur,Category
class PieceSerializer(serializers.ModelSerializer):
    class Meta:  
        model = Piece
        fields = '__all__'

class  CategorySerializer(serializers.ModelSerializer):
    class Meta:  
        model = Category
        fields = '__all__'


class DemandeMaterielSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandeMateriel
        fields = '__all__'

class FablabInscriptionUtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = FablabInscriptionUtilisateur
        fields = '__all__'
