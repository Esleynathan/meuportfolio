from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer para o model Contact.
    Usado para receber mensagens via formulário de contato.
    """

    class Meta:
        model = Contact
        fields = [
            'id',
            'name',
            'email',
            'subject',
            'message',
            'read',
            'created_at',
        ]
        read_only_fields = ['id', 'read', 'created_at']

    def validate_email(self, value):
        """
        Validação customizada de email.
        """
        if not value:
            raise serializers.ValidationError("E-mail é obrigatório.")
        return value.lower()  # Normaliza para minúsculas
