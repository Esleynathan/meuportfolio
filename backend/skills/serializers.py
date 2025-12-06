from rest_framework import serializers
from .models import Skill


class SkillSerializer(serializers.ModelSerializer):
    """
    Serializer para o model Skill.
    Transforma dados do banco em JSON e vice-versa.
    """

    # Campos que retornam os labels legíveis (ex: "Frontend" em vez de "frontend")
    category_display = serializers.CharField(source='get_category_display', read_only=True)
    proficiency_level_display = serializers.CharField(source='get_proficiency_level_display', read_only=True)

    class Meta:
        model = Skill
        fields = [
            'id',
            'name',
            'category',
            'category_display',  # "Frontend", "Backend", etc.
            'proficiency_level',
            'proficiency_level_display',  # "Básico", "Avançado", etc.
            'icon',
            'order',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']
