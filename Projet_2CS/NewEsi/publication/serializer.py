# serializers.py
from rest_framework import serializers
from .models import Utilisateur,Publication , Token ,MembreClub,Club , Partenaire , Demande_Partenariat, Devis, Partenaire_labo, Laboratoire, Equipe_Recherche, Equipe_Projet, Projet, Theme_Recherche , Administration_Annuaire , Annuaire , Alumnie_Annuaire , Enseignant_Annuaire , Question, Reponse

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields ='__all__'
        #fields = ['id', 'email', 'family_name', 'first_name', 'is_active', 'date_joined', 'last_login']
class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'
class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'
class MembreSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembreClub
        fields = '__all__'  # Sérialiser tous les champs du modèle

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






# #recherche

class LaboratoireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratoire
        fields = ['id_laboratoire', 'nom', 'description']

class Partenaire_laboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partenaire_labo
        fields = ['nom', 'description', 'contact', 'email', 'laboratoire']

# class ChercheurSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Chercheur
#         fields = ['email','id', 'family_name', 'first_name', 'equipe']

class Equipe_RechercheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe_Recherche
        fields = ['id_equipe_recherche', 'nom', 'laboratoire', 'theme']

class Equipe_ProjetSerializer(serializers.ModelSerializer):
    #Chercheur = serializers.PrimaryKeyRelatedField(many=True, queryset=Chercheur.objects.all())  # Assuming Chercheur is the related model
    Chercheur =serializers.PrimaryKeyRelatedField(queryset=Utilisateur.objects.filter(is_chercheur=True), many=True, required=False)
    class Meta:
        model = Equipe_Projet
        fields = ['id_equipe_projet', 'nom', 'Chercheur', 'laboratoire']

class ProjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projet
        fields = ['id_projet', 'nom', 'description', 'equipe_projet']

class Theme_RechercheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme_Recherche
        fields = ['id_theme', 'nom', 'description','themes']








class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class ReponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reponse
        fields = '__all__'


class AnnuaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annuaire
        fields = '__all__'

class AdministrationAnnuaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administration_Annuaire
        fields = '__all__'

class EnseignantAnnuaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enseignant_Annuaire
        fields = '__all__'

class AlumnieAnnuaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumnie_Annuaire
        fields = '__all__'
        