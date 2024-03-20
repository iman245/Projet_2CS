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
        if param_value:
            queryset = Utilisateur.objects.all()
            serializer = UtilisateurSerializer(queryset, many=True)
            return Response(serializer.data)

    def post(self, request):
        param_value = request.query_params.get('add_users')
        if param_value:
            serializer = UtilisateurSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        param_value = request.query_params.get('edit_users')
        if param_value:
            serializer = UtilisateurSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       