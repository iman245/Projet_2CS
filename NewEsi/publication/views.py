from django.shortcuts import render
from .models import Utilisateur, Publication
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
def users_list(request):
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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return any validation errors