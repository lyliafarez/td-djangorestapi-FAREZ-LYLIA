# serializers.py

from rest_framework import serializers
from .models import ProjetDeRecherche, Chercheur, Publication

class ProjetDeRechercheSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjetDeRecherche
        fields = '__all__'

class ChercheurSerializer(serializers.ModelSerializer):
    projects = ProjetDeRechercheSerializer(many=True, read_only=True)

    class Meta:
        model = Chercheur
        fields = '__all__'
        
class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'
