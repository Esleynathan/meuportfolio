from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Configuração do admin para o model Contact.
    """
    list_display = ['name', 'email', 'subject', 'read', 'created_at']
    list_filter = ['read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    list_editable = ['read']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'

    fieldsets = (
        ('Remetente', {
            'fields': ('name', 'email')
        }),
        ('Mensagem', {
            'fields': ('subject', 'message')
        }),
        ('Status', {
            'fields': ('read', 'created_at')
        }),
    )

    def has_add_permission(self, request):
        """
        Desabilita criação manual de contatos.
        Contatos só devem ser criados via API.
        """
        return False
