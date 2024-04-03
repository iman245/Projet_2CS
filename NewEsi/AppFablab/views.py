from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from publication.decorators import user_types_required
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.db.models import Q
from django.core.mail import send_mail
from publication.models import Utilisateur
from django.conf import settings
from datetime import datetime



@api_view(['GET'])
def get_all_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@user_types_required('responsable_fablab')
def add_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@user_types_required('responsable_fablab')
def update_category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = CategorySerializer(category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@user_types_required('responsable_fablab')
def delete_category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    category.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@user_types_required('responsable_fablab')
def ajouter_piece(request):
    if request.method == 'POST':
        
        categories = Category.objects.all()
        
        categorie_id = request.data.get('categorie_id', None)
        if categorie_id:
            try:
              
                categorie = Category.objects.get(pk=categorie_id)
            except Category.DoesNotExist:
                return Response({"error": "La catégorie sélectionnée n'existe pas."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Veuillez sélectionner une catégorie."}, status=status.HTTP_400_BAD_REQUEST)

      
        request.data['categorie'] = categorie.pk

        serializer = PieceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_pieces(request):
    if request.method == 'GET':
       
        pieces = Piece.objects.filter(quantite_disponible__gt=0)  
        serializer = PieceSerializer(pieces, many=True)

        return Response(serializer.data)
    
@api_view(['DELETE'])
@user_types_required('responsable_fablab')
def supprimer_piece(request, piece_id):
    piece = get_object_or_404(Piece, id_piece=piece_id)
    if request.method == 'DELETE':
        piece.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['PUT', 'PATCH'])
@user_types_required('responsable_fablab')
def modifier_piece(request, piece_id):
    piece = get_object_or_404(Piece, id_piece=piece_id)

    if request.method == 'PUT' or request.method == 'PATCH':
        serializer = PieceSerializer(piece, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

 
@api_view(['GET'])
def get_all_categories_fablab(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
def pieces_by_category(request):
    if request.method == 'GET':
      
        categories = Category.objects.all()

        category_data = []
        for category in categories:
            category_pieces = Piece.objects.filter(categorie=category, quantite_disponible__gt=0)
            category_serializer = PieceSerializer(category_pieces, many=True)
            category_data.append({
                'category': CategorySerializer(category).data,
                'pieces': category_serializer.data
            })

        return Response(category_data)
    




@api_view(['GET'])
def search_piece_by_name(request):
    if request.method == 'GET':
      
        nom_piece = request.GET.get('nom', None)

        if nom_piece:
           
            pieces = Piece.objects.filter(Q(nom__icontains=nom_piece))

          
            serializer = PieceSerializer(pieces, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "Veuillez fournir un nom de pièce valide dans le paramètre 'nom'."}, status=400)
        


@api_view(['GET'])
def filter_pieces_by_category(request):
    if request.method == 'GET':
        
        categorie_id = request.GET.get('categorie', None)

        if categorie_id:
            
            pieces = Piece.objects.filter(categorie=categorie_id, quantite_disponible__gt=0)

          
            serializer = PieceSerializer(pieces, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "Veuillez fournir l'ID de la catégorie dans le paramètre 'categorie'."}, status=400)
        



@api_view(['GET'])
def filter_pieces_by_state(request):
    if request.method == 'GET':
        
        etat_param = request.GET.get('etat', None)

      
        if etat_param is not None:
            if etat_param.lower() == 'true':
                etat_bool = True
            elif etat_param.lower() == 'false':
                etat_bool = False
            else:
                return Response({"error": "Le paramètre 'etat' doit être 'true' ou 'false'."}, status=400)

          
            pieces = Piece.objects.filter(etat=etat_bool)

         
            serializer = PieceSerializer(pieces, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "Veuillez fournir un paramètre 'etat' pour filtrer les pièces ('true' pour oui, 'false' pour non)."}, status=400)



@api_view(['POST'])

def faire_demande_materiel(request):
    if request.method == 'POST':
        serializer = DemandeMaterielSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['GET'])
@user_types_required('responsable_fablab')
def get_all_demandes_materiel(request):
    if request.method == 'GET':
        demandes_materiel = DemandeMateriel.objects.all()
        serializer = DemandeMaterielSerializer(demandes_materiel, many=True)
        return Response(serializer.data)
    


@api_view(['POST'])
@user_types_required('responsable_fablab')
def accepter_rejeter_demande(request, demande_id):
    try:
        demande = DemandeMateriel.objects.get(pk=demande_id)
    except DemandeMateriel.DoesNotExist:
        return Response({"error": "La demande de matériel spécifiée n'existe pas."}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':
        statut = request.data.get('statut', None)
        
      
        if not demande.piece.etat:
            return Response({"error": "La pièce demandée n'est pas disponible."}, status=status.HTTP_400_BAD_REQUEST)

       
        if statut == 'REJETEE' or not demande.piece.etat:
            demande.status = 'REJETEE'
            demande.save()
            sujet = "Réponse sur votre demande"
            message = f"Cher {demande.nom},\n\n"
            message += f"votre demande de matériel a été rejetée: {demande.piece.nom}.\n"
            message += "Merci !"

            send_mail(
                subject=sujet,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[demande.email],   
                fail_silently=True,
            )
            return Response({"message": "La demande de matériel a été rejetée."}, status=status.HTTP_200_OK)
        
        
       
        if statut == 'VALIDEE':
            piece = demande.piece
            quantite_empruntee = demande.quantite_empruntee

            if piece.quantite_disponible < quantite_empruntee:
                return Response({"error": "La quantité disponible de la pièce est insuffisante."}, status=status.HTTP_400_BAD_REQUEST)

            piece.quantite_disponible -= quantite_empruntee
            if piece.quantite_disponible == 0:
                piece.etat = False

            piece.save()
            sujet = "Réponse sur votre demande"
            message = f"Cher {demande.nom},\n\n"
            message += f"votre demande de matériel a été validée: {demande.piece.nom}.\n"
            message += "Merci !"

            send_mail(
                subject=sujet,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[demande.email],  
                fail_silently=True,
            )
       
        demande.status = statut
        demande.save()
        return Response({"message": f"Demande de matériel {demande.status}."}, status=status.HTTP_200_OK)


@api_view(['GET'])
def filtrer_demandes_par_statut(request, statut):
    if request.method == 'GET':
        demandes = DemandeMateriel.objects.filter(status=statut)
        serializer = DemandeMaterielSerializer(demandes, many=True)
        return Response(serializer.data)
    
@api_view(['POST'])
def inscription_utilisateur(request):
    if request.method == 'POST':
        serializer = FablabInscriptionUtilisateurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@user_types_required('responsable_fablab')
def get_all_inscriptions(request):
    if request.method == 'GET':
        inscriptions = FablabInscriptionUtilisateur.objects.all()
        serializer = FablabInscriptionUtilisateurSerializer(inscriptions, many=True)
        return Response(serializer.data)
    


@api_view(['POST'])
def save_piece(request, id_piece):
    if request.method == 'POST':
        user = request.user
        piece = get_object_or_404(Piece, pk=id_piece)
        
        saved_piece, created = UserSavedPiece.objects.get_or_create(user=user, piece=piece)
        if created:
            return Response({"message": "Piece saved successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Piece already saved"}, status=status.HTTP_200_OK)
        


@api_view(['GET'])
def piece_info(request, piece_id):
    try:
        piece = Piece.objects.get(pk=piece_id)
    except Piece.DoesNotExist:
        return Response({"error": "Piece not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = PieceInfoSerializer(piece, context={'request': request})
    return Response(serializer.data)



@api_view(['GET'])
@user_types_required('responsable_fablab')
def filter_inscriptions_by_date(request):
    if request.method == 'GET':
     
        start_date_str = request.query_params.get('start_date', None)
        end_date_str = request.query_params.get('end_date', None)
        

        if start_date_str:
            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            except ValueError:
                return Response({"error": "Invalid start date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            start_date = datetime.min
        
        if end_date_str:
            try:
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
            except ValueError:
                return Response({"error": "Invalid end date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            end_date = datetime.max

   
        inscriptions = FablabInscriptionUtilisateur.objects.filter(created__range=[start_date, end_date])
        
 
        serializer = FablabInscriptionUtilisateurSerializer(inscriptions, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@user_types_required('responsable_fablab')
def filter_demandes_by_date(request):
    if request.method == 'GET':
        start_date_str = request.query_params.get('start_date', None)
        end_date_str = request.query_params.get('end_date', None)
        
        if start_date_str:
            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            except ValueError:
                return Response({"error": "Invalid start date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            start_date = datetime.min
        
        if end_date_str:
            try:
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
            except ValueError:
                return Response({"error": "Invalid end date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            end_date = datetime.max

        demandes = DemandeMateriel.objects.filter(date_emprunt__range=[start_date, end_date])
        
        serializer = DemandeMaterielSerializer(demandes, many=True)
        return Response(serializer.data)