"""
URL configuration for NewEsi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from publication.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', get_all_users, name='get_all_users'),  # URL for getting all users and creating new users
    path('users/edit/<int:pk>/', edit_user, name='edit_user'),  # URL for editing a specific user
    path('users/search/', search_user, name='search_user'),  # URL for searching users by name
    path('users/add',add_user,name='add_user'),
    path('users/login',login_user,name='login_user'),
    path('users/delete/<int:pk>/',delete_user,name='delete_user'),
    path('publication/', get_all_publications, name='get_all_publications'),
    path('publication/add/', add_publication, name='add_publication'),
    path('publication/validate/<int:pk>/', validate_publication, name='validate_publication'),
    path('publication/refuse/<int:pk>/', refuse_publication, name='validate_publication'),
    path('publication/<int:pk>/', edit_publication, name='edit_publication'),
    path('publication/search/',search_publication,name='search_publication'),
    path('publication/delete/<int:pk>/', delete_publication, name='delete_publication'),
    path('partenaire/add',add_partenaire,name='add_partenaire'),
    path('partenaires',get_all_partenaire,name='get_all_partenaire'),
    path('partenaire',get_partenaire,name='get_partenaire'),
    path('demande_partenariat',post_demande_partenariat,name='demande_partenariat'),
    path('demande_partenariat/all',get_all_demande_partenariat,name='get_all_demande_partenariat'),
    path('demande_partenariat/accepter',accepter_demande_partenariat,name='accepter_demande_partenariat'),
    path('demande_partenariat/refuser',refuser_demande_partenariat,name='refuser_demande_partenariat'),
    path('Devis/valider',valider_devis,name='valider_devis'),
    path('Devis/demande',add_devis,name='add_devis'),
    path('Devis',get_all_devis,name='get_all_devis'),
    path('chercheur',chercheur_list,name='chercheur'),
    path('partenair_labo',partenaire_labo_list,name='partenaire_labo_list'),
    path('labos',laboratoire_list,name='laboratoire_list'),
    path('equipe_recherche',equipe_recherche_list,name='equipe_recherche_list'),
    path('chercheur',chercheur_list,name='chercheur'),
    path('equipe_projet',equipe_projet_list,name='equipe_projet'),
    path('theme',theme_recherche_list,name='theme'),
    path('project',projet_list,name='project'),
    path('club/<int:club_id>/', get_club_members, name='get_club_members'),
    path('club/<int:club_id>/add_member/', add_club_member, name='add_club_member'),
    path('club/<int:club_id>/update/', update_club, name='update_club'),
    path('club/<int:club_id>/delete/', delete_club, name='delete_club'),
    path('club/<int:club_id>/members/<int:member_id>/update/', update_member, name='update_member'),
    path('club/<int:club_id>/members/<int:member_id>/delete/', delete_member, name='delete_member'),
    path('club/<int:club_id>/members/<str:name>/', get_members_by_name, name='get_members_by_name'),
    path('club/<str:name>/',get_clubs_by_name, name='get_clubs_by_name'),
    path('club/<int:club_id>/evenement_publications/', get_club_evenement_publications, name='get_club_evenement_publications'),
    path('club/<int:club_id>/add_evenement_publication/', add_evenement_publication_to_club, name='add_evenement_publication_to_club'),
    path('', include('AppFablab.urls')),
        path('poser-question/', PoserQuestion, name='poser_question'),
    path('repondre-question/<int:question_id>/', RepondreQuestion, name='repondre_question'),
    path('questions/<str:category>', GetQuestions, name='GetQuestions'),
    path('annuaire/', get_all_annuaire , name='get_all_directory_entries'),
    path('annuaire/add/',add_annuaire, name='add_directory_entry'),
    path('annuaire/<int:pk>/', get_Annuaire, name='get_directory_entry'),
    path('annuaire/edit/<int:pk>/', edit_Annuaire, name='edit_directory_entry'),
    path('annuaire/delete/<int:pk>/', delete_Annuaire, name='delete_directory_entry'),
    path('annuaire/enseignant/filter/', filter_enseignant_by_grade_and_mot_cle, name='filter_enseignant'),
    path('annuaire/administration/filter/', filter_administration_by_mot_cle_and_service, name='filter_administration'),
    path('annuaire/alumnie/filter/', filter_alumnie_by_promotion, name='filter_alumnie'),
    path('annuaire/grades/', get_all_grades, name='get_all_grades'),
    path('annuaire/promotions/', get_all_promotions, name='get_all_promotions'),
    path('annuaire/services/', get_all_services, name='get_all_services'),
]

