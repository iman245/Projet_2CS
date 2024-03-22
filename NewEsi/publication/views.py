from django.shortcuts import render
from .models import Utilisateur, Publication
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.decorators import api_view
from django.db.models import Q
@api_view(['GET'])
def get_all_users(request):
    if request.method == 'GET':
        queryset = Utilisateur.objects.all()
        serializer = UtilisateurSerializer(queryset, many=True)
        return Response(serializer.data)
    
@api_view(['POST'])  
def add_user(request):
    if request.method == 'POST':
        data = request.data.copy()  # Create a copy of the request data
        data.pop('id', None)  # Remove 'id' field if present
        if isinstance(data, list):  # If data is an array
            serializer = UtilisateurSerializer(data=data, many=True)
        else:  # If data is a single object
            serializer = UtilisateurSerializer(data=data)
       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
def add_publication(request):
    if request.method == 'POST':
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