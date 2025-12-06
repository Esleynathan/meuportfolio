import { Component, OnInit } from '@angular/core';
import { SkillsService } from '../../services/skills.service';
import { Skill } from '../../models/skill.model';
import { TranslationService } from '../../services/translation.service';

@Component({
  selector: 'app-skills',
  templateUrl: './skills.component.html',
  styleUrls: ['./skills.component.css']
})
export class SkillsComponent implements OnInit {
  skills: Skill[] = [];
  isLoading = true;
  error: string | null = null;

  constructor(
    private skillsService: SkillsService,
    private translationService: TranslationService
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
      },
      error: (err) => {
        this.error = this.translationService.translate('skills.error');
        this.isLoading = false;
        console.error('Erro ao buscar skills:', err);
      }
    });
  }

  handleImageError(event: Event): void {
    // Se a imagem falhar ao carregar, esconde o elemento img
    const imgElement = event.target as HTMLImageElement;
    imgElement.style.display = 'none';
  }
}
