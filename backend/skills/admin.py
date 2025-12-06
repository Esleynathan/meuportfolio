from django.contrib import admin
from .models import Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """
    Configuração do admin para o model Skill.
    """
    list_display = ['name', 'category', 'proficiency_level', 'order']
    list_filter = ['category', 'proficiency_level']
    search_fields = ['name']
    list_editable = ['order']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('name', 'category', 'proficiency_level')
        }),
        ('Mídia', {
            'fields': ('icon',)
        }),
        ('Configurações', {
            'fields': ('order',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
