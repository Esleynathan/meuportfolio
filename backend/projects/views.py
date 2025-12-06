from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
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
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'technologies']
    ordering_fields = ['order', 'created_at']
    ordering = ['order', '-created_at']  # Ordenação padrão

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """
        Endpoint customizado que retorna apenas projetos em destaque.
        GET /api/projects/featured/
        """
        featured_projects = self.queryset.filter(featured=True)
        serializer = self.get_serializer(featured_projects, many=True)
        return Response(serializer.data)
