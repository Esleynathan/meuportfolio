from django.db import models


class Skill(models.Model):
    """
    Model para habilidades e tecnologias.
    Armazena tecnologias dominadas e nível de proficiência.
    """

    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('devops', 'DevOps'),
        ('database', 'Database'),
        ('tools', 'Ferramentas'),
        ('other', 'Outros'),
    ]

    PROFICIENCY_CHOICES = [
        ('basic', 'Básico'),
        ('intermediate', 'Intermediário'),
        ('advanced', 'Avançado'),
        ('expert', 'Expert'),
    ]

    # Informações básicas
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nome",
        help_text="Nome da tecnologia ou habilidade"
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='other',
        verbose_name="Categoria",
        help_text="Categoria da habilidade"
    )

    proficiency_level = models.CharField(
        max_length=20,
        choices=PROFICIENCY_CHOICES,
        default='intermediate',
        verbose_name="Nível de proficiência",
        help_text="Nível de domínio da tecnologia"
    )

    # Ícone/Logo
    icon = models.ImageField(
        upload_to='skills/',
        blank=True,
        null=True,
        verbose_name="Ícone",
        help_text="Logo ou ícone da tecnologia"
    )

    # Configurações
    order = models.IntegerField(
        default=0,
        verbose_name="Ordem",
        help_text="Ordem de exibição"
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
        verbose_name = "Habilidade"
        verbose_name_plural = "Habilidades"
        ordering = ['category', 'order', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"
