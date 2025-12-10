from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Contact
from .serializers import ContactSerializer


@method_decorator(csrf_exempt, name='dispatch')
class ContactViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar mensagens de contato via API REST.

    Endpoints disponíveis:
    - GET  /api/contacts/     → Lista mensagens (apenas admin)
    - POST /api/contacts/     → Envia nova mensagem (público)
    - GET  /api/contacts/{id}/ → Detalhes de uma mensagem
    """

    queryset = Contact.objects.all().order_by('-created_at')
    serializer_class = ContactSerializer
    http_method_names = ['get', 'post', 'head', 'options']  # Desabilita PUT, PATCH, DELETE via API

    def get_permissions(self):
        """
        Define permissões diferentes por ação.
        - Ação de criação ('create') é pública para receber mensagens.
        - Outras ações ('list', 'retrieve') exigem login de admin para ler as mensagens.
        """
        if self.action == 'create':
            # Qualquer um pode enviar uma mensagem
            permission_classes = [AllowAny]
        else:
            # Apenas administradores podem listar ou ver as mensagens
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        """
        Sobrescreve o método create para personalizar a resposta.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response({
            'message': 'Mensagem enviada com sucesso! Entraremos em contato em breve.',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)
