from .serializers import ToDOSerializer
from .models import ToDo
from rest_framework import viewsets



class ToDAPIViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDOSerializer