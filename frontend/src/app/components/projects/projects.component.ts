import { Component, OnInit } from '@angular/core';
import { ProjectsService } from '../../services/projects.service';
import { Project } from '../../models/project.model';
import { TranslationService } from '../../services/translation.service';

@Component({
  selector: 'app-projects',
  templateUrl: './projects.component.html',
  styleUrls: ['./projects.component.css']
})
export class ProjectsComponent implements OnInit {
  projects: Project[] = [];
  isLoading = true;
  error: string | null = null;

  constructor(
    private projectsService: ProjectsService,
    private translationService: TranslationService
  ) {}

  ngOnInit(): void {
    this.loadProjects();
  }

  loadProjects(): void {
    this.isLoading = true;
    this.error = null;

    this.projectsService.getProjects().subscribe({
      next: (data) => {
        this.projects = data;
        this.isLoading = false;
      },
      error: (err) => {
        this.error = this.translationService.translate('projects.error');
        this.isLoading = false;
        console.error('Erro ao buscar projetos:', err);
      }
    });
  }

  handleImageError(event: Event): void {
    // Se a imagem falhar ao carregar, esconde o elemento img
    const imgElement = event.target as HTMLImageElement;
    imgElement.style.display = 'none';
  }
}
