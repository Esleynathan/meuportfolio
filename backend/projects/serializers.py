from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer para o model Project.
    Transforma dados do banco em JSON e vice-versa.
    """

    # Campo customizado que retorna lista de tecnologias
    technologies_list = serializers.SerializerMethodField()

    # Campo customizado que retorna o label da categoria
    category_display = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'slug',
            'description',
            'detailed_description',
            'image',
            'technologies',
            'technologies_list',  # Campo adicional com lista
            'category',
            'category_display',  # Campo adicional com label legível
            'github_url',
            'live_url',
            'featured',
            'order',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['slug', 'created_at', 'updated_at']

    def get_technologies_list(self, obj):
        """
        Retorna technologies como lista em vez de string.
        Ex: "Django, React, PostgreSQL" → ["Django", "React", "PostgreSQL"]
        """
        return obj.get_technologies_list()

    def get_category_display(self, obj):
        """
        Retorna o label legível da categoria.
        Ex: "automation" → "Automação"
        """
        return obj.get_category_display()
