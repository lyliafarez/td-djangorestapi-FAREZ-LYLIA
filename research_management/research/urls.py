from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    ProjetDeRechercheListView,ProjetDeRechercheListCreateView, ProjetDeRechercheDetailView,
    ProjetDeRechercheUpdateView, ProjetDeRechercheDeleteView,
    ChercheurListView,ChercheurListCreateView, ChercheurDetailView,
    ChercheurUpdateView, ChercheurDeleteView,
    PublicationListView,PublicationListCreateView, PublicationDetailView,
    PublicationUpdateView, PublicationDeleteView
)
router = DefaultRouter()

urlpatterns = [
    # URLs for ProjetDeRecherche
    path('projetslist/', ProjetDeRechercheListView.as_view(), name='projet-list'),
    path('projets/', ProjetDeRechercheListCreateView.as_view(), name='projet-list-create'),
    path('projets/<int:pk>/', ProjetDeRechercheDetailView.as_view(), name='projet-detail'),
    path('projets/update/<int:pk>/', ProjetDeRechercheUpdateView.as_view(), name='projet-update'),
    path('projets/delete/<int:pk>/', ProjetDeRechercheDeleteView.as_view(), name='projet-delete'),
    
    # URLs for Chercheur
    path('', ChercheurListView.as_view(), name='home'),
    path('chercheurslist/', ChercheurListView.as_view(), name='chercheur-list'),
    path('chercheurs/', ChercheurListCreateView.as_view(), name='chercheur-list-create'),
    path('chercheurs/<int:pk>/', ChercheurDetailView.as_view(), name='chercheur-detail'),
    path('chercheurs/update/<int:pk>/', ChercheurUpdateView.as_view(), name='chercheur-update'),
    path('chercheurs/delete/<int:pk>/', ChercheurDeleteView.as_view(), name='chercheur-delete'),
    
    # URLs for Publication
     path('publicationslist/', PublicationListView.as_view(), name='publication-list'),
    path('publications/', PublicationListCreateView.as_view(), name='publication-list-create'),
    path('publications/<int:pk>/', PublicationDetailView.as_view(), name='publication-detail'),
    path('publications/update/<int:pk>/', PublicationUpdateView.as_view(), name='publication-update'),
    path('publications/delete/<int:pk>/', PublicationDeleteView.as_view(), name='publication-delete'),
]
