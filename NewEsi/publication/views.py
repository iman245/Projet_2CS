from django.shortcuts import render,get_object_or_404
from .models import Utilisateur, Publication
from .serializer import *
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import AllowAny
from django.db.models import Q
from .decorators import *
@api_view(['GET'])
def get_all_users(request):
    if request.method == 'GET':
        queryset = Utilisateur.objects.all()
        serializer = UtilisateurSerializer(queryset, many=True)
        return Response(serializer.data)
    
@api_view(['POST']) 
@permission_classes([AllowAny])   
def add_user(request):
    if request.method == 'POST':
        data = request.data.copy()  # Create a copy of the request data
        data.pop('id', None)  # Remove 'id' field if present
        # if isinstance(data, list):  # If data is an array
        #     serializer = UtilisateurSerializer(data=data, many=True)
        # else:  # If data is a single object
        serializer = UtilisateurSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    if request.method == 'POST':
        email = request.data.get('email', None)

        if not email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)
        if Utilisateur.objects.filter(email=email).exists():
            user = Utilisateur.objects.get(email=email)
        else:
            user = Utilisateur.objects.create(email=email)

        token = Token.objects.get(user=user)
        return Response({"token": token.key}, status=status.HTTP_200_OK if user else status.HTTP_201_CREATED)

        
@api_view(['PUT'])
def edit_user(request, pk):
    try:
        user = Utilisateur.objects.get(pk=pk)
    except Utilisateur.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        data = request.data.copy()  # Create a copy of the request data
        data.pop('id', None)  # Remove 'id' field if present
        serializer = UtilisateurSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def search_user(request):
    if request.method == 'GET':
        query_params = request.query_params
        filters = {}

        # Iterate over query parameters
        for key, value in query_params.items():
            # Exclude the 'query' parameter
            if key != 'query' and value:
                # Add filter condition if the field is not empty
                filters[key + '__icontains'] = value

        if filters:
            # Construct Q objects for filtering
            conditions = [Q(**{key: value}) for key, value in filters.items()]
            # Combine Q objects using OR operator
            users = Utilisateur.objects.filter(*conditions)
        else:
            # If no filters are provided, return all users
            users = Utilisateur.objects.all()

        serializer = UtilisateurSerializer(users, many=True)
        return Response(serializer.data)
    else:
        return Response("Invalid request method", status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['DELETE'])
def delete_user(request, pk):
    try:
        user = Utilisateur.objects.get(pk=pk)
    except Utilisateur.DoesNotExist:
        return Response("User not found", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        user.delete()
        return Response("User deleted successfully", status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_publications_by_category(request, category):
    try:
        publications = Publication.objects.filter(category=category)
    except Publication.DoesNotExist:
        return Response("Publications not found for this category", status=status.HTTP_404_NOT_FOUND)

    serializer = PublicationSerializer(publications, many=True)
    return Response(serializer.data)

#This is for publication
    
@api_view(['GET'])
def get_all_publications(request):
    if request.method == 'GET':
        queryset = Publication.objects.all()
        serializer = PublicationSerializer(queryset, many=True)
        return Response(serializer.data)

# POST a new publication
@api_view(['POST'])
@user_types_required('editeur')
def add_publication(request):
    if request.method == 'POST':
        # Check if user is an editor
            if isinstance(request.data, list):  # If data is an array
                serializer = PublicationSerializer(data=request.data, many=True)
            else:  # If data is a single object
                serializer = PublicationSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def search_publication(request):
    if request.method == 'GET':
        query_params = request.query_params
        filters = {}

        # Iterate over query parameters
        for key, value in query_params.items():
            # Exclude the 'query' parameter
            if key != 'query' and value:
                # Add filter condition if the field is not empty
                filters[key + '__icontains'] = value

        if filters:
            # Construct Q objects for filtering
            conditions = [Q(**{key: value}) for key, value in filters.items()]
            # Combine Q objects using OR operator
            publications = Publication.objects.filter(*conditions)
        else:
            # If no filters are provided, return all publications
            publications = Publication.objects.all()

        serializer = PublicationSerializer(publications, many=True)
        return Response(serializer.data)
    else:
        return Response("Invalid request method", status=status.HTTP_405_METHOD_NOT_ALLOWED)
# PUT edit a publication by ID
@api_view(['PUT'])
def edit_publication(request, pk):
    try:
        publication = Publication.objects.get(pk=pk)
    except Publication.DoesNotExist:
        return Response("Publication not found", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PublicationSerializer(publication, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT'])
@user_types_required('adminstrateur')
def validate_publication(request, pk):
    try:
        publication = Publication.objects.get(pk=pk)

    except Publication.DoesNotExist:
        return Response("Publication not found", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        # Update the 'etat' attribute to 'valide'
        publication.etat = 'valide'
        # Save the changes to the publication object
        publication.save()

        # Serialize the updated publication object
        serializer = PublicationSerializer(publication)
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response("Invalid request method", status=status.HTTP_405_METHOD_NOT_ALLOWED)
# DELETE a publication by ID
@api_view(['DELETE'])
def delete_publication(request, pk):
    try:
        publication = Publication.objects.get(pk=pk)
    except Publication.DoesNotExist:
        return Response("Publication not found", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        publication.delete()
        return Response("Publication deleted successfully", status=status.HTTP_204_NO_CONTENT)    


#club
# Get all members of a club
@api_view(['GET'])
def get_club_members(request, club_id):
    if request.method == 'GET':
        try:
            club = Club.objects.get(id_club=club_id)
        except Club.DoesNotExist:
            return Response("Club not found", status=status.HTTP_404_NOT_FOUND)
        
        members = club.membres.all()
        serializer = MembreSerializer(members, many=True)
        return Response(serializer.data)

# Add a member to a club
@api_view(['POST'])
def add_club_member(request, club_id):
    if request.method == 'POST':
        try:
            club = Club.objects.get(id_club=club_id)
        except Club.DoesNotExist:
            return Response("Club not found", status=status.HTTP_404_NOT_FOUND)

        serializer = MembreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(club=club)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get all clubs
@api_view(['GET'])
def get_all_clubs(request):
    if request.method == 'GET':
        clubs = Club.objects.all()
        serializer = ClubSerializer(clubs, many=True)
        return Response(serializer.data)

# Create a new club
@api_view(['POST'])
def create_club(request):
    if request.method == 'POST':
        serializer = ClubSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


# Update a Club
@api_view(['PUT'])

def update_club(request, club_id):
    club = get_object_or_404(Club, id_club=club_id)
    if request.method == 'PUT':
        serializer = ClubSerializer(club, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete a Club
@api_view(['DELETE'])

def delete_club(request, club_id):
    club = get_object_or_404(Club, id_club=club_id)
    if request.method == 'DELETE':
        club.delete()
        return Response("Club deleted successfully", status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_club_evenement_publications(request, club_id):
    club = get_object_or_404(Club, id_club=club_id)
    if request.method == 'GET':
        publications = club.publications.all()
        serializer = PublicationSerializer(publications, many=True)
        return Response(serializer.data)

# Add a publication of type 'evenement' to a club
@api_view(['POST'])

def add_evenement_publication_to_club(request, club_id):
    club = get_object_or_404(Club, id_club=club_id)
    if request.method == 'POST':
        data = request.data.copy()
        data['club'] = club.id_club
        serializer = PublicationSerializer(data=data)
        if serializer.is_valid():
            if serializer.validated_data['type_publication'] != 'evenement':
                return Response("Publication type must be 'evenement'", status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update a Member
@api_view(['PUT'])

def update_member(request, member_id):
    member = get_object_or_404(MembreClub, id_membre=member_id)
    if request.method == 'PUT':
        serializer = MembreSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete a Member
@api_view(['DELETE'])
def delete_member(request, member_id):
    member = get_object_or_404(MembreClub, id_membre=member_id)
    if request.method == 'DELETE':
        member.delete()
        return Response("Member deleted successfully", status=status.HTTP_204_NO_CONTENT)

# Get Members by Name
@api_view(['GET'])
def get_members_by_name(request, club_id, name):
    if request.method == 'GET':
        club = get_object_or_404(Club, id_club=club_id)
        members = club.membres.filter(nom__icontains=name)
        serializer = MembreSerializer(members, many=True)
        return Response(serializer.data)

# Get Clubs by Name
@api_view(['GET'])
def get_clubs_by_name(request, name):
    if request.method == 'GET':
        clubs = Club.objects.filter(nom__icontains=name)
        serializer = ClubSerializer(clubs, many=True)
        return Response(serializer.data)



@api_view(['POST'])

def add_partenaire(request):
   if request.method == 'POST':
        if isinstance(request.data, list):  # If data is an array
            serializer = PartenaireSerializer(data=request.data, many=True)
        else:  # If data is a single object
            serializer = PartenaireSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_partenaire(request):
    if request.method == 'GET':
        queryset = Partenaire.objects.all()
        serializer = PartenaireSerializer(queryset, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_partenaire(request):
    partenaire_id = request.query_params.get('id')
    if partenaire_id is None:
        return Response("ID du partenaire manquant dans les paramètres de requête", status=status.HTTP_400_BAD_REQUEST)
    
    try:
        partenaire = Partenaire.objects.get(pk=partenaire_id)
        serializer = PartenaireSerializer(partenaire)
        return Response(serializer.data)
    except Partenaire.DoesNotExist:
        return Response("Partenaire introuvable", status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def post_demande_partenariat(request):
    if request.method == 'POST':
        serializer = DemandePartenariatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_all_demande_partenariat(request):
    if request.method == 'GET':
        demandes = Demande_Partenariat.objects.all()
        serializer = DemandePartenariatSerializer(demandes, many=True)
        return Response(serializer.data)


@api_view(['PUT'])
def accepter_demande_partenariat(request):
    demande_id = request.query_params.get('id')
    if demande_id is None:
        return Response("ID de la demande de partenariat manquant", status=status.HTTP_400_BAD_REQUEST)
    try:
        demande = Demande_Partenariat.objects.get(pk=demande_id)
        demande.etat = 'Acceptée'
        demande.save()
        nom_partenaire = demande.nom
        description_partenaire = demande.description
        contact_partenaire = demande.contact
        email_partenaire = demande.email
        partenaire = Partenaire.objects.create(nom=nom_partenaire, description=description_partenaire, contact=contact_partenaire, email=email_partenaire)

        return Response("Demande de partenariat acceptée et le partenaire ajouté", status=status.HTTP_200_OK)
    except Demande_Partenariat.DoesNotExist:
        return Response("Demande de partenariat introuvable", status=status.HTTP_404_NOT_FOUND)



@api_view(['PUT'])
def refuser_demande_partenariat(request):
    demande_id = request.query_params.get('id')
    if demande_id is None:
        return Response("ID de la demande de partenariat manquant", status=status.HTTP_400_BAD_REQUEST)
    try:
        demande = Demande_Partenariat.objects.get(pk=demande_id)
        demande.etat = 'Refusée'
        demande.save()
        return Response("Demande de partenariat refusée", status=status.HTTP_200_OK)
    except Demande_Partenariat.DoesNotExist:
        return Response("Demande de partenariat introuvable", status=status.HTTP_404_NOT_FOUND)




@api_view(['POST'])
def add_devis(request):
    if request.method == 'POST':
        serializer = DevisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def valider_devis(request):
    devis_id = request.query_params.get('devis_id')
    if devis_id is None:
        return Response("ID du devis manquant", status=status.HTTP_400_BAD_REQUEST)
    
    try:
        devis = Devis.objects.get(pk=devis_id)
        devis.etat = 'Validé'
        devis.save()
        return Response("Devis validé", status=status.HTTP_200_OK)
    except Devis.DoesNotExist:
        return Response("Devis introuvable", status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def get_all_devis(request):
    if request.method == 'GET':
        queryset = Devis.objects.all()
        serializer = DevisSerializer(queryset, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])

def partenaire_labo_list(request):
    if request.method == 'GET':
        queryset = Partenaire_labo.objects.all()
        serializer = Partenaire_laboSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Partenaire_laboSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def laboratoire_list(request):
    if request.method == 'GET':
        queryset = Laboratoire.objects.all()
        serializer = LaboratoireSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LaboratoireSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def chercheur_list(request):
    if request.method == 'GET':
        queryset = Utilisateur.objects.filter(is_chercheur=True)
        serializer = UtilisateurSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UtilisateurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



# @api_view(['GET', 'POST'])
# def equipe_projet_list(request):
#     if request.method == 'GET':
#         queryset = Equipe_Projet.objects.all()
#         serializer = Equipe_ProjetSerializer(queryset, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = Equipe_ProjetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
    
@api_view(['GET', 'POST'])
def equipe_projet_list(request):
    if request.method == 'GET':
        # Assuming you want to filter equipe by authenticated Chercheur
        if request.user.is_authenticated and request.user.is_chercheur:
            equipe = Equipe_Projet.objects.filter(Chercheur=request.user)
            serializer = Equipe_ProjetSerializer(equipe, many=True)
            return Response(serializer.data)
        else:
            return Response("You are not authorized to access this resource.", status=status.HTTP_403_FORBIDDEN)
    elif request.method == 'POST':
        # You can add authorization logic here if required
        serializer = Equipe_ProjetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

@api_view(['GET', 'POST'])
def equipe_recherche_list(request):
    if request.method == 'GET':
        queryset = Equipe_Recherche.objects.all()
        serializer = Equipe_RechercheSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Equipe_RechercheSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def projet_list(request):
    if request.method == 'GET':
        queryset = Projet.objects.all()
        serializer = ProjetSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProjetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def theme_recherche_list(request):
    if request.method == 'GET':
        queryset = Theme_Recherche.objects.all()
        serializer = Theme_RechercheSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Theme_RechercheSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)








































'''def users_list(request):
    users = Utilisateur.objects.all()  # Retrieve all users from the database
    return render(request, 'users_list.html', {'users': users})

def publication_detail(request, publication_id):
    publication = Publication.objects.get(id_publication=publication_id)  # Retrieve a specific publication
    return render(request, 'publication_detail.html', {'publication': publication})



class UtilisateurAPIView(APIView):
    def get(self, request):
        param_value = request.query_params.get('all_users')
        
        queryset = Utilisateur.objects.all()
        serializer = UtilisateurSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        
        serializer = UtilisateurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditUserAPIView(APIView):
  def post(self, request, pk):  # Accept the user ID as a URL parameter
        user = Utilisateur.objects.get(pk=pk)  # Get the user object based on the provided ID
        serializer = UtilisateurSerializer(user, data=request.data)  # Initialize the serializer with the user object and request data
        if serializer.is_valid():
            serializer.save()  # Save the changes to the user object
            return Response(serializer.data, status=status.HTTP_200_OK)  # Return the updated user data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return any validation errors '''