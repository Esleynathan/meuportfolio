from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import Skill
from .serializers import SkillSerializer


class SkillViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar habilidades via API REST.

    Endpoints disponíveis:
    - GET    /api/skills/       → Lista todas as habilidades
    - POST   /api/skills/       → Cria nova habilidade
    - GET    /api/skills/{id}/  → Detalhes de uma habilidade
    - PUT    /api/skills/{id}/  → Atualiza habilidade
    - DELETE /api/skills/{id}/  → Deleta habilidade
    """

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['category', 'order', 'name']
    ordering = ['category', 'order', 'name']  # Ordenação padrão
    filterset_fields = ['category', 'proficiency_level']  # Permite filtrar por categoria

    def get_permissions(self):
        """
        Define permissões diferentes por ação.
        - Ações de leitura ('list', 'retrieve') são públicas.
        - Outras ações ('create', 'update', 'destroy') exigem login de admin.
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
