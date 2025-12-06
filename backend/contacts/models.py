from django.db import models


class Contact(models.Model):
    """
    Model para mensagens de contato.
    Armazena mensagens enviadas pelo formulário de contato.
    """

    # Dados do remetente
    name = models.CharField(
        max_length=200,
        verbose_name="Nome",
        help_text="Nome completo do remetente"
    )

    email = models.EmailField(
        verbose_name="E-mail",
        help_text="E-mail do remetente"
    )

    # Mensagem
    subject = models.CharField(
        max_length=300,
        verbose_name="Assunto",
        help_text="Assunto da mensagem"
    )

    message = models.TextField(
        verbose_name="Mensagem",
        help_text="Conteúdo da mensagem"
    )

    # Status
    read = models.BooleanField(
        default=False,
        verbose_name="Lida",
        help_text="Mensagem foi lida?"
    )

    # Timestamps
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Recebida em"
    )

    class Meta:
        verbose_name = "Mensagem de Contato"
        verbose_name_plural = "Mensagens de Contato"
        ordering = ['-created_at']  # Mais recentes primeiro

    def __str__(self):
        status = "✓" if self.read else "✗"
        return f"{status} {self.name} - {self.subject}"
