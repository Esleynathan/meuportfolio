from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar projetos via API REST.

    Endpoints disponíveis:
    - GET    /api/projects/          → Lista todos os projetos
    - POST   /api/projects/          → Cria novo projeto
    - GET    /api/projects/{id}/     → Detalhes de um projeto
    - PUT    /api/projects/{id}/     → Atualiza projeto
    - DELETE /api/projects/{id}/     → Deleta projeto
    - GET    /api/projects/featured/ → Lista apenas projetos em destaque
    - GET    /api/projects/?category=automation → Filtra por categoria
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'featured']
    search_fields = ['title', 'description', 'technologies']
    ordering_fields = ['order', 'created_at', 'category']
    ordering = ['order', '-created_at']  # Ordenação padrão

    def get_permissions(self):
        """
        Define permissões diferentes por ação.
        - Ações de leitura ('list', 'retrieve', 'featured') são públicas.
        - Outras ações ('create', 'update', 'destroy') exigem login de admin.
        """
        if self.action in ['list', 'retrieve', 'featured']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """
        Endpoint customizado que retorna apenas projetos em destaque.
        GET /api/projects/featured/
        """
        featured_projects = self.queryset.filter(featured=True)
        serializer = self.get_serializer(featured_projects, many=True)
        return Response(serializer.data)
