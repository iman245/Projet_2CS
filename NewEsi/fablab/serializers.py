from rest_framework import serializers
from models import *
class DemandeMaterielSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandeMateriel
        fields ='__all__'

class PieceElectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PieceElect
        fields ='__all__'

