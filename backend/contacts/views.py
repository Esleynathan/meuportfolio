from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar mensagens de contato via API REST.

    Endpoints disponíveis:
    - GET  /api/contacts/     → Lista mensagens (apenas admin)
    - POST /api/contacts/     → Envia nova mensagem (público)
    - GET  /api/contacts/{id}/ → Detalhes de uma mensagem
    """

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    http_method_names = ['get', 'post', 'head', 'options']  # Desabilita PUT, PATCH, DELETE via API

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
