from rest_framework import serializers
from fablab.models import *
class DemandeMaterielSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandeMateriel
        fields ='__all__'

class PieceElectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PieceElect
        fields ='__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields ='__all__'
