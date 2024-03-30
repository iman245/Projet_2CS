from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import DemandeMateriel, PieceElect
from .serializers import DemandeMaterielSerializer, PieceElectSerializer
from publication.decorators import user_types_required

# Get all material requests
@api_view(['GET'])
@user_types_required('responsable_fablab')
def get_all_material_requests(request):
    if request.method == 'GET':
        requests = DemandeMateriel.objects.all()
        serializer = DemandeMaterielSerializer(requests, many=True)
        return Response(serializer.data)

# Accept or reject a material request
@api_view(['PUT'])
@user_types_required('responsable_fablab')
def accept_or_reject_material_request(request, request_id):
    request_instance = get_object_or_404(DemandeMateriel, id_demandeur=request_id)
    if request.method == 'PUT':
        data = request.data.copy()
        serializer = DemandeMaterielSerializer(request_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get all electrical pieces associated with a material request
@api_view(['GET'])
@user_types_required('responsable_fablab')
def get_electrical_pieces_for_material_request(request, request_id):
    request_instance = get_object_or_404(DemandeMateriel, id_demandeur=request_id)
    if request.method == 'GET':
        electrical_pieces = PieceElect.objects.filter(demande_materiel=request_instance)
        serializer = PieceElectSerializer(electrical_pieces, many=True)
        return Response(serializer.data)

# Add an electrical piece to a material request
@api_view(['POST'])
def add_electrical_piece_to_material_request(request, request_id):
    request_instance = get_object_or_404(DemandeMateriel, id_demandeur=request_id)
    if request.method == 'POST':
        data = request.data.copy()
        data['demande_materiel'] = request_instance.id_demandeur
        serializer = PieceElectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
