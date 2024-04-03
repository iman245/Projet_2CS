from rest_framework import serializers
from .models import Piece, DemandeMateriel, FablabInscriptionUtilisateur,Category
from .models import UserSavedPiece

class UserSavedPieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSavedPiece
        fields = '__all__'

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


class PieceInfoSerializer(serializers.ModelSerializer):
    categorie_name = serializers.CharField(source='categorie.name')
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Piece
        fields = ['nom', 'categorie_name', 'photo_url', 'etat', 'quantite_disponible']

    def get_photo_url(self, piece):
        request = self.context.get('request')
        photo_url = piece.photo.url
        return request.build_absolute_uri(photo_url)