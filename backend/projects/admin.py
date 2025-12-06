from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Configuração do admin para o model Project.
    """
    list_display = ['title', 'featured', 'order', 'created_at']
    list_filter = ['featured', 'created_at']
    search_fields = ['title', 'description', 'technologies']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['featured', 'order']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('title', 'slug', 'description', 'detailed_description')
        }),
        ('Mídia', {
            'fields': ('image',)
        }),
        ('Tecnologias e Links', {
            'fields': ('technologies', 'github_url', 'live_url')
        }),
        ('Configurações', {
            'fields': ('featured', 'order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
