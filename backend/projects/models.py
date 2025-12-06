from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    """
    Model para projetos do portfólio.
    Armazena informações sobre projetos desenvolvidos.
    """

    # Informações básicas
    title = models.CharField(
        max_length=200,
        verbose_name="Título",
        help_text="Título do projeto"
    )
    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True,
        help_text="URL amigável (gerado automaticamente)"
    )

    # Descrições
    description = models.CharField(
        max_length=300,
        verbose_name="Descrição curta",
        help_text="Resumo do projeto (exibido em cards)"
    )
    detailed_description = models.TextField(
        verbose_name="Descrição detalhada",
        help_text="Descrição completa do projeto"
    )

    # Imagem
    image = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True,
        verbose_name="Imagem de capa",
        help_text="Imagem principal do projeto"
    )

    # Tecnologias (lista separada por vírgula)
    technologies = models.CharField(
        max_length=500,
        verbose_name="Tecnologias",
        help_text="Tecnologias usadas (separadas por vírgula). Ex: Django, React, PostgreSQL"
    )

    # Links
    github_url = models.URLField(
        blank=True,
        null=True,
        verbose_name="Link do GitHub",
        help_text="URL do repositório no GitHub"
    )
    live_url = models.URLField(
        blank=True,
        null=True,
        verbose_name="Link do projeto",
        help_text="URL do projeto em produção"
    )

    # Configurações
    featured = models.BooleanField(
        default=False,
        verbose_name="Destacar",
        help_text="Exibir na página inicial?"
    )
    order = models.IntegerField(
        default=0,
        verbose_name="Ordem",
        help_text="Ordem de exibição (menor número aparece primeiro)"
    )

    # Timestamps
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Criado em"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Atualizado em"
    )

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        ordering = ['order', '-created_at']  # Ordena por ordem, depois por data (mais recente)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Gera slug automaticamente a partir do título"""
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_technologies_list(self):
        """Retorna lista de tecnologias"""
        return [tech.strip() for tech in self.technologies.split(',')]
