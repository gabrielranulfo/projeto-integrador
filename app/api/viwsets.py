from rest_framework import viewsets,permissions
from app.api import serializers
from app import models

class CadMapViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CadMapSerializer
    queryset = models.Cad_Mapeamento.objects.all()
    permission_classes = [permissions.IsAuthenticated]
class CadSetoresViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CadSetoresSerializer
    queryset = models.Cad_setores.objects.all()
    permission_classes = [permissions.IsAuthenticated]
class CadEquipesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CadEquipesSerializer
    queryset = models.Cad_equipes.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class ItensAuditaveisViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ItensAuditaveisSerializer
    queryset = models.Cad_itens_auditaveis.objects.all()
    permission_classes = [permissions.IsAuthenticated]