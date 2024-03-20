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
from django.urls import path
from publication import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.users_list, name='users_list'),  # URL for listing users
    path('users/', views.UtilisateurAPIView.as_view(), name='user-list'),
    path('users/edit/<int:pk>/', views.EditUserAPIView.as_view(), name='user-edit'),
    path('publication/<int:publication_id>/', views.publication_detail, name='publication_detail'),  # URL for publication detail with ID
]
