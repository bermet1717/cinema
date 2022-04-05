from django.shortcuts import render

# Create your views here.

from rest_framework.generics import *
from applications.films.models import Films
from applications.films.serializers import FilmsSerializer

class ListCreateView(ListCreateAPIView):
    queryset = Films.objects.all()
    serializer_class = FilmsSerializer


class DeleteUpdateRetrieveView(RetrieveUpdateDestroyAPIView):
    queryset = Films.objects.all()
    serializer_class = FilmsSerializer