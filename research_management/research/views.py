from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
from rest_framework.response import Response
from .models import ProjetDeRecherche, Chercheur, Publication
from .serializers import ProjetDeRechercheSerializer, ChercheurSerializer, PublicationSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.views.generic import ListView, DetailView
from .forms import ChercheurForm, ProjetDeRechercheForm, PublicationForm

# ProjetDeRecherche views
class ProjetDeRechercheListView(ListView):
    model = ProjetDeRecherche
    template_name = 'project/index.html'  # Correct template path
    context_object_name = 'projets' 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['titre']

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(titre__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context
        
class ProjetDeRechercheListCreateView(generics.ListCreateAPIView):
    queryset = ProjetDeRecherche.objects.all()
    serializer_class = ProjetDeRechercheSerializer
    def get(self, request, *args, **kwargs):
        form = ProjetDeRechercheForm()
        return render(request, 'project/projet_create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ProjetDeRechercheForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projet-list')  # Redirect to Chercheur list view
        return render(request, 'project/projet_create.html', {'form': form})


class ProjetDeRechercheDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjetDeRecherche.objects.all()
    serializer_class = ProjetDeRechercheSerializer
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        #projects = ProjetDeRecherche.objects.filter(chef_de_projet=instance)
        #project_serializer = ProjetDeRechercheSerializer(projects, many=True)
        data = serializer.data
        #data['projects'] = project_serializer.data
        return render(request, 'project/projet_detail.html', {'projet': data})

    
class ProjetDeRechercheUpdateView(generics.RetrieveUpdateAPIView):
    queryset = ProjetDeRecherche.objects.all()
    serializer_class = ProjetDeRechercheSerializer
    partial = True
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        form = ProjetDeRechercheForm(instance=instance)
        return render(request, 'project/projet_update.html', {'form': form})

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        form = ProjetDeRechercheForm(request.POST, instance=instance)
        form.save()
        return redirect('projet-list')  # Redirect to Chercheur list view after update
        #return render(request, 'researcher/chercheur_update.html', {'form': form})

    
class ProjetDeRechercheDeleteView(generics.DestroyAPIView):
    queryset = ProjetDeRecherche.objects.all()
    serializer_class = ProjetDeRechercheSerializer

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return redirect('projet-list')

# Chercheur views
""" class ChercheurListView(ListView):
    model = Chercheur
    template_name = 'researcher/index.html'  # Correct template path
    context_object_name = 'chercheurs' 

    def get_queryset(self):
        return Chercheur.objects.all() """
class ChercheurListView(ListView):
    model = Chercheur
    template_name = 'researcher/index.html'
    context_object_name = 'chercheurs'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nom', 'specialite']

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(nom__icontains=search_query) | queryset.filter(specialite__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context

""" class ChercheurListCreateView(generics.ListCreateAPIView):
    queryset = Chercheur.objects.all()
    serializer_class = ChercheurSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['nom', 'specialite']
    search_fields = ['nom', 'specialite']
    
 """
class ChercheurListCreateView(generics.ListCreateAPIView):
    queryset = Chercheur.objects.all()
    serializer_class = ChercheurSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['nom', 'specialite']
    search_fields = ['nom', 'specialite']

    def get(self, request, *args, **kwargs):
        form = ChercheurForm()
        return render(request, 'researcher/chercheur_create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ChercheurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chercheur-list')  # Redirect to Chercheur list view
        return render(request, 'researcher/chercheur_create.html', {'form': form})


""" class ChercheurDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chercheur.objects.all()
    serializer_class = ChercheurSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['nom', 'specialite']
    search_fields = ['nom', 'specialite']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        projects = ProjetDeRecherche.objects.filter(chef_de_projet=instance)
        project_serializer = ProjetDeRechercheSerializer(projects, many=True)
        data = serializer.data
        data['projects'] = project_serializer.data
        return Response(data) """

class ChercheurDetailView(generics.RetrieveAPIView):
    queryset = Chercheur.objects.all()
    serializer_class = ChercheurSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        projects = ProjetDeRecherche.objects.filter(chef_de_projet=instance)
        project_serializer = ProjetDeRechercheSerializer(projects, many=True)
        data = serializer.data
        data['projects'] = project_serializer.data
        return render(request, 'researcher/chercheur_detail.html', {'chercheur': data})

""" class ChercheurUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Chercheur.objects.all()
    serializer_class = ChercheurSerializer
    partial = True """

class ChercheurUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Chercheur.objects.all()
    serializer_class = ChercheurSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        form = ChercheurForm(instance=instance)
        return render(request, 'researcher/chercheur_update.html', {'form': form})

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        form = ChercheurForm(request.POST, instance=instance)
        form.save()
        return redirect('chercheur-list')  # Redirect to Chercheur list view after update
        #return render(request, 'researcher/chercheur_update.html', {'form': form})

""" class ChercheurDeleteView(generics.DestroyAPIView):
    queryset = Chercheur.objects.all()
    serializer_class = ChercheurSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response("Chercheur deleted.") """
class ChercheurDeleteView(generics.DestroyAPIView):
    queryset = Chercheur.objects.all()
    serializer_class = ChercheurSerializer

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return redirect('chercheur-list')

# Publication views

class PublicationListView(ListView):
    model = Publication
    template_name = 'publication/index.html'  # Correct template path
    context_object_name = 'publications' 

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['titre']

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(titre__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context

class PublicationListCreateView(generics.ListCreateAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    def get(self, request, *args, **kwargs):
        form = PublicationForm()
        return render(request, 'publication/publication_create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = PublicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publication-list')  # Redirect to publication list view
        return render(request, 'publication/publication_create.html', {'form': form})


class PublicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer   
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)    
        data = serializer.data
        return render(request, 'publication/publication_detail.html', {'publication': data})
 

class PublicationUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    partial = True
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        form = PublicationForm(instance=instance)
        return render(request, 'publication/publication_update.html', {'form': form})

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        form = PublicationForm(request.POST, instance=instance)
        form.save()
        return redirect('publication-list') 
    
class PublicationDeleteView(generics.DestroyAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return redirect('publication-list')