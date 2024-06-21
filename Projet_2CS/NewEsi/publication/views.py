from django.conf import settings
from django.shortcuts import render,get_object_or_404
from .models import *
from .serializer import *
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import AllowAny
from django.db.models import Q
from .decorators import *
from django.core.mail import send_mail
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine
from langchain_community.agent_toolkits import create_sql_agent
import pandas as pd
from langchain_community.llms import HuggingFaceEndpoint
from transformers import AutoTokenizer, AutoModelForCausalLM

import json
@api_view(['GET'])
@permission_classes([AllowAny])
def query_publications(request):
    query = request.GET.get('query', '')
    results = []
    HUGGINGFACEHUB_API_TOKEN =  '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'
    if query:
        df=pd.read_csv(r'C:\Users\Dell\Desktop\Projet_2CS\Projet_2CS\NewEsi\publication\Data\events.csv')
        df.rename(columns={'Concatenated': 'events'}, inplace=True)

        #df=pd.read_csv(r'C:\Users\Dell\Desktop\Projet_2CS\Projet_2CS\NewEsi\publication\Data\events.csv')
        # engine = create_engine("sqlite:///events.db")
        # try:
        #     df.to_sql("events", engine)
        # except:
        #     pass    
        # db = SQLDatabase(engine=engine)
        

        # tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B")
        # model = AutoModelForCausalLM.from_pretrained("meta-llama/Meta-Llama-3-8B")
        # model=pipeline( model=model)
        llm = HuggingFaceEndpoint(
        huggingfacehub_api_token='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',
        repo_id = "mistralai/Mistral-7B-Instruct-v0.2",
        # repo_id="Xenova/gpt-4o",
        max_new_tokens=512,
        top_k=10,
        top_p=0.95,
        typical_p=0.95,
        temperature=0.01,
        repetition_penalty=1.03,
        streaming=True,
    )
        # agent_executor = create_sql_agent(llm, db=db, verbose=True,handle_parsing_errors=True)
        
        # response = agent_executor.invoke({"input": f"{query} ## Answer one answer that fits the best"})
        # results = response['output']
        df_json = df.to_json(orient='records')

        # Include JSON string in the input data
        input_data = {
            'input': f"{query} ## Answer one answer that fits the best and is most close to the question from the following data. Don't answer outside the data, look at all data before answering and if there is no information in the data say: 'there is no information in the database to answer your question' #### Data= {df_json}"
        }

        input_data_str = json.dumps(input_data)

        # Invoke the language model with the input data string
        results = llm.invoke(input_data_str)
        # results=model(input_data_str)
    data = {
        'query': query,
        'results': results[:-4]
    }
    serializer = PublicationQuerySerializer(data=data)
    if serializer.is_valid():
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET'])
@user_types_required('adminstrateur')
def get_all_users(request):
    if request.method == 'GET':
        queryset = Utilisateur.objects.all()
        serializer = UtilisateurSerializer(queryset, many=True)
        return Response(serializer.data)
    
@api_view(['POST']) 
# @user_types_required('adminstrateur')  
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
        password = request.data.get('password', None)
        
        if not password :
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)
        if not email:
            return Response({"error": "password  is required"}, status=status.HTTP_400_BAD_REQUEST)
        if Utilisateur.objects.filter(email=email , password = password).exists():
            user = Utilisateur.objects.get(email=email )
            token = Token.objects.get(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK if user else status.HTTP_201_CREATED)
        if Utilisateur.objects.filter(email=email).exists():
            return Response({"error": "mot de passe incorrect"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Vous n'avez pas de compte"}, status=status.HTTP_404_NOT_FOUND)

        
@api_view(['PUT'])
@user_types_required('adminstrateur')
def edit_user(request, pk):
    try:
        user = Utilisateur.objects.get(pk=pk)
    except Utilisateur.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        data = request.data.copy()  # Create a copy of the request data
        data.pop('id', None)  # Remove 'id' field if present
        serializer = UtilisateurSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@user_types_required('adminstrateur')
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
@user_types_required('adminstrateur')
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

@api_view(['POST'])
@user_types_required('editeur')
def add_event(request):
    if request.method == 'POST':
        request.data['publisher'] = request.user.id
        cat_id = request.data['categorie']
        category = Categorie.objects.get(id=cat_id)
        user = Utilisateur.objects.filter(is_admin=True, categorie=category).first()
        if user is None:
            return Response({"error": "No admin user found for this category"}, status=status.HTTP_400_BAD_REQUEST)
        
        request.data['type_publication'] = 'event'
        request.data['etat'] = 'en attente'
        serializer = PublicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            sujet = "Demande de publication"
            
            message = f"Une nouvelle demande de publication est insérée, intitulé: {request.data['titre']}.\n"
            message += "en attendant votre validation "
            message += "Merci !"

            send_mail(
                subject=sujet,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],   
                fail_silently=True,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@user_types_required('editeur')
def add_actualité(request):
    if request.method == 'POST':

        request.data['type_publication'] = 'actualité'
        request.data['etat']='en attente'
        serializer = PublicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def create_categorie(request):
    if request.method == 'POST':
        serializer = CategorieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_categorie(request, categorie_id):
    try:
        categorie = Categorie.objects.get(pk=categorie_id)
    except Categorie.DoesNotExist:
        return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
    
    categorie.delete()
    return Response({"success": "Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])

@api_view(['GET'])
@permission_classes([AllowAny])
def search_publication(request):
    if request.method == 'GET':
        query_params = request.query_params
        auth_header = request.headers.get('Authorization')
        token_key = auth_header.split(' ')[1]
        
        try:
            user = Token.objects.get(key=token_key).user
        except Token.DoesNotExist:
            return Response({"user.id"}, status=status.HTTP_400_BAD_REQUEST)
        filters = {}
        publisher = None
        
        
        
        # Iterate over query parameters
        for key, value in query_params.items():
            if key == 'publisher' and value:
                publisher = value
            elif key != 'query' and value:
                # Add filter condition if the field is not empty
                filters[key + '__icontains'] = value
        
        if publisher:
            publications = Publication.objects.filter(publisher_id=publisher)
            if filters:
                conditions = [Q(**{key: value}) for key, value in filters.items()]
                publications = publications.filter(*conditions)
        else:
            if filters:
                # Construct Q objects for filtering
                conditions = [Q(**{key: value}) for key, value in filters.items()]
                # Combine Q objects using AND operator
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
@user_types_required('editeur')
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


@api_view(['PUT'])
@user_types_required('adminstrateur')
def refuse_publication(request, pk):
    try:
        publication = Publication.objects.get(pk=pk)
    except Publication.DoesNotExist:
        return Response("Publication not found", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        publication.etat = 'refuse'
        publication.save()
        serializer = PublicationSerializer(publication)
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response("Invalid request method", status=status.HTTP_405_METHOD_NOT_ALLOWED)




# DELETE a publication by ID
@api_view(['DELETE'])
@user_types_required('adminstrateur')
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
@user_types_required('editeur')
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
@user_types_required('adminstrateur')
def create_club(request):
    if request.method == 'POST':
        serializer = ClubSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


# Update a Club
@api_view(['PUT'])
@user_types_required('editeur')
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
@user_types_required('adminstrateur')
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
@user_types_required('editeur')
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
@user_types_required('editeur')
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
@user_types_required('adminstrateur')
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
@user_types_required('directeur_relex')
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
@user_types_required('directeur_relex')
def get_all_demande_partenariat(request):
    if request.method == 'GET':
        demandes = Demande_Partenariat.objects.all()
        serializer = DemandePartenariatSerializer(demandes, many=True)
        return Response(serializer.data)


@api_view(['PUT'])
@user_types_required('directeur_relex')
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
@user_types_required('directeur_relex')
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
@user_types_required('directeur_relex')
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
@user_types_required('directeur_relex')
def get_all_devis(request):
    if request.method == 'GET':
        queryset = Devis.objects.all()
        serializer = DevisSerializer(queryset, many=True)
        return Response(serializer.data)

@api_view(['POST'])
@user_types_required('adminstrateur')
def add_partenaire_labo(request):
    if  request.method == 'POST':
        serializer = Partenaire_laboSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def partenaire_labo_list(request):
    if request.method == 'GET':
        queryset = Partenaire_labo.objects.all()
        serializer = Partenaire_laboSerializer(queryset, many=True)
        return Response(serializer.data)      


@api_view(['GET'])
def laboratoire_list(request):
    if request.method == 'GET':
        queryset = Laboratoire.objects.all()
        serializer = LaboratoireSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view([ 'POST'])
@user_types_required('adminstrateur')
def add_laboratoire(request):
   
    if request.method == 'POST':
        serializer = LaboratoireSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)






@api_view(['POST'])
@user_types_required('adminstrateur')
def add_chercheur(request):
    
    if request.method == 'POST':
        serializer = UtilisateurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



@api_view(['GET'])
def chercheur_list(request):
    if request.method == 'GET':
        queryset = Utilisateur.objects.filter(is_chercheur=True)
        serializer = UtilisateurSerializer(queryset, many=True)
        return Response(serializer.data)
    


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
    
@api_view(['GET'])
def equipe_projet_list(request):
    if request.method == 'GET':
        # Assuming you want to filter equipe by authenticated Chercheur
        if request.user.is_authenticated and request.user.is_chercheur:
            equipe = Equipe_Projet.objects.filter(Chercheur=request.user)
            serializer = Equipe_ProjetSerializer(equipe, many=True)
            return Response(serializer.data)
        else:
            return Response("You are not authorized to access this resource.", status=status.HTTP_403_FORBIDDEN)
    


@api_view([ 'POST'])
@user_types_required('adminstrateur')
def add_equipe_projet(request):
    if request.method == 'POST':
        # You can add authorization logic here if required
        serializer = Equipe_ProjetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


@api_view(['POST'])
@user_types_required('adminstrateur')
def add_equipe_recherche(request):
   if request.method == 'POST':
        serializer = Equipe_RechercheSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET'])
def equipe_recherche_list(request):
    if request.method == 'GET':
        queryset = Equipe_Recherche.objects.all()
        serializer = Equipe_RechercheSerializer(queryset, many=True)
        return Response(serializer.data)
    

@api_view(['POST'])
@user_types_required('editeur')
def add_projet(request):
   if request.method == 'POST':
        serializer = ProjetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET'])

def projet_list(request):
    if request.method == 'GET':
        queryset = Projet.objects.all()
        serializer = ProjetSerializer(queryset, many=True)
        return Response(serializer.data)
   

@api_view(['POST'])
@user_types_required('adminstrateur')
def add_theme_recherche(request):
   if request.method == 'POST':
        serializer = Theme_RechercheSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET'])
def theme_recherche_list(request):
    if request.method == 'GET':
        queryset = Theme_Recherche.objects.all()
        serializer = Theme_RechercheSerializer(queryset, many=True)
        return Response(serializer.data)
   


@api_view(['POST'])
def PoserQuestion( request):
     serializer = QuestionSerializer(data=request.data)
     if serializer.is_valid():
            serializer.save(auteur=request.user)  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view([ 'POST'])
@user_types_required('adminstrateur')
def RepondreQuestion( request, question_id):
        question = Question.objects.get(pk=question_id)
        serializer = ReponseSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save( question=question)
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view([ 'GET'])
def GetQuestions(request, category):
     questions = Question.objects.filter(category=category)
     data = []
     for question in questions:
        reponses = Reponse.objects.filter(question=question)
        reponses_data = []
        for reponse in reponses:
            reponses_data.append({
                'reponse_texte': reponse.contenu,
            })
        data.append({
            'question': question.contenu,
            'reponses': reponses_data
        })
     return Response(data)





@api_view(['POST'])
@user_types_required('adminstrateur')
def add_annuaire(request):
    if request.method == 'POST':
        category = request.data.get('category')
        if category == 'admin':
            serializer = AdministrationAnnuaireSerializer(data=request.data)
        elif category == 'enseignant':
            serializer = EnseignantAnnuaireSerializer(data=request.data)
        elif category == 'alumnie':
            serializer = AlumnieAnnuaireSerializer(data=request.data)
        else:
            return Response("Invalid category", status=status.HTTP_400_BAD_REQUEST)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Invalid request method", status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def get_all_annuaire(request):
    annuaires = Annuaire.objects.all()
    serializer = AnnuaireSerializer(annuaires, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_Annuaire(request, pk):
    try:
        entry = Annuaire.objects.get(pk=pk)
        serializer = AnnuaireSerializer(entry)
        return Response(serializer.data)
    except Annuaire.DoesNotExist:
        return Response("Entry not found", status=status.HTTP_404_NOT_FOUND)





@api_view(['PUT'])
@user_types_required('adminstrateur')
def edit_Annuaire(request, pk):
    try:
        entry = Annuaire.objects.get(pk=pk)
        if request.method == 'PUT':
            serializer = AnnuaireSerializer(entry, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Annuaire.DoesNotExist:
        return Response("Entry not found", status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@user_types_required('adminstrateur')
def delete_Annuaire(request, pk):
    try:
        entry = Annuaire.objects.get(pk=pk)
        if request.method == 'DELETE':
            entry.delete()
            return Response("Entry deleted successfully", status=status.HTTP_204_NO_CONTENT)
    except Annuaire.DoesNotExist:
        return Response("Entry not found", status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def filter_enseignant_by_grade_and_mot_cle(request):
    grade = request.query_params.get('grade')
    mot_cle = request.query_params.get('mot_cle')
    if grade and mot_cle:
        enseignants = Enseignant_Annuaire.objects.filter(grade=grade, mot_cle__icontains=mot_cle)
    elif grade:
        enseignants = Enseignant_Annuaire.objects.filter(grade=grade)
    elif mot_cle:
        enseignants = Enseignant_Annuaire.objects.filter(mot_cle__icontains=mot_cle)
    else:
        enseignants = Enseignant_Annuaire.objects.all()  
    serializer = EnseignantAnnuaireSerializer(enseignants, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def filter_administration_by_mot_cle_and_service(request):
    service= request.query_params.get('service')
    mot_cle = request.query_params.get('mot_cle')
    if service and mot_cle:
        admin = Administration_Annuaire.objects.filter(service=service, mot_cle__icontains=mot_cle)
    elif service :
        admin = Administration_Annuaire.objects.filter(service=service)
    elif mot_cle:
        admin = Administration_Annuaire.objects.filter(mot_cle__icontains=mot_cle)
    else:
        admin = Administration_Annuaire.objects.all()  
    serializer = AdministrationAnnuaireSerializer(admin, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def filter_alumnie_by_promotion(request):
    promotion= request.query_params.get('promotion')
    mot_cle = request.query_params.get('mot_cle')
    if promotion and mot_cle:
        Alumnie = Alumnie_Annuaire.objects.filter(promotion=promotion, mot_cle__icontains=mot_cle)
    elif promotion :
        Alumnie = Alumnie_Annuaire.objects.filter(promotion=promotion)
    elif mot_cle:
        Alumnie = Alumnie_Annuaire.objects.filter(mot_cle__icontains=mot_cle)
    else:
        Alumnie= Alumnie_Annuaire.objects.all()  
    serializer = AlumnieAnnuaireSerializer(Alumnie, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def get_all_grades(request):
    grades_set = set(choice[1] for choice in Enseignant_Annuaire.GRADE_CHOICES)
    grades_list = list(grades_set)
    return Response({'grades': grades_list})


@api_view(['GET'])
def get_all_promotions(request):
    promotions = Alumnie_Annuaire.objects.values_list('promotion', flat=True).distinct()
    return Response({'promotions': promotions})

@api_view(['GET'])
def get_all_services(request):
    services = Administration_Annuaire.objects.values_list('service', flat=True).distinct()
    return Response({'services': services})























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
