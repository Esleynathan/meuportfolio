import { Component, OnInit } from '@angular/core';
import { Skill } from '../../models/skill.model';
import { SkillsService } from '../../services/skills.service';
import { TranslationService } from '../../services/translation.service';

@Component({
  selector: 'app-skills',
  templateUrl: './skills.component.html',
  styleUrls: ['./skills.component.css']
})
export class SkillsComponent implements OnInit {
  skills: Skill[] = [];
  groupedSkills: { [key: string]: Skill[] } = {};
  isLoading = true;
  error: string | null = null;

  // Mapeamento de ícones para categorias
  categoryIcons: { [key: string]: string } = {
    'Frontend': 'fas fa-laptop-code',
    'Backend': 'fas fa-server',
    'DevOps & Ferramentas': 'fas fa-tools',
    'default': 'fas fa-cogs'
  };

  // Mapeamento de chaves da API para nomes de exibição
  private categoryDisplayMap: { [key: string]: string } = {
    'frontend': 'Frontend',
    'backend': 'Backend',
    'devops': 'DevOps & Ferramentas',
    'tools': 'DevOps & Ferramentas',
    'database': 'Database',
    'other': 'Outros'
  };

  // Mapeamento de níveis de proficiência para % e nome de exibição
  private proficiencyConfig: { [key: string]: { width: number; label: string } } = {
    'basic': { width: 40, label: 'Básico' },
    'intermediate': { width: 60, label: 'Intermediário' },
    'advanced': { width: 80, label: 'Avançado' },
    'expert': { width: 100, label: 'Expert' }
  };

  constructor(
    private skillsService: SkillsService,
    public translationService: TranslationService
  ) {}

  ngOnInit(): void {
    this.loadSkills();
  }

  loadSkills(): void {
    this.isLoading = true;
    this.error = null;

    this.skillsService.getSkills().subscribe({
      next: (data) => {
        this.skills = data;
        this.isLoading = false;
        this.groupSkillsByCategory();
      },
      error: (err) => {
        this.error = this.translationService.translate('skills.error');
        this.isLoading = false;
      }
    });
  }

  groupSkillsByCategory(): void {
    this.groupedSkills = this.skills.reduce((acc, skill) => {
      const apiCategory = skill.category || 'other';
      const category = this.categoryDisplayMap[apiCategory] || 'Outros';

      if (!acc[category]) {
        acc[category] = [];
      }
      acc[category].push(skill);
      return acc;
    }, {} as { [key: string]: Skill[] });

  }

  handleImageError(event: Event): void {
    // Se a imagem falhar ao carregar, esconde o elemento img
    const imgElement = event.target as HTMLImageElement;
    imgElement.style.display = 'none';
  }

  getGroupedSkillsKeys(): string[] {
    // Ordena as chaves (categorias) com base no campo 'order' da primeira skill de cada grupo.
    // Isso garante que as categorias apareçam na ordem definida no admin.
    return Object.keys(this.groupedSkills).sort((a, b) => {
      const orderA = this.groupedSkills[a][0]?.order ?? Infinity;
      const orderB = this.groupedSkills[b][0]?.order ?? Infinity;
      return orderA - orderB;
    });
  }

  getProficiencyWidth(level: string | number): number {
    return this.proficiencyConfig[String(level)]?.width || 0;
  }

  getProficiencyLabel(level: string | number): string {
    return this.proficiencyConfig[level]?.label || '';
  }
}
