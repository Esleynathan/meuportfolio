import { Component, HostListener, OnInit } from '@angular/core';
import { Title, Meta } from '@angular/platform-browser';
import { TranslateService } from './services/translate.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  showBackToTop = false;

  constructor(
    private titleService: Title,
    private metaService: Meta,
    private translateService: TranslateService
  ) {}

  ngOnInit(): void {
    // Define o título e a meta descrição padrão
    this.translateService.get('seo.title').subscribe((title: string) => {
      this.titleService.setTitle(title);
    });
    this.translateService.get('seo.description').subscribe((description: string) => {
      this.metaService.updateTag({ name: 'description', content: description });
    });

    // Inicializa o estado do botão baseado na posição atual do scroll
    this.checkScrollPosition();
  }

  @HostListener('window:scroll', [])
  onWindowScroll(): void {
    this.checkScrollPosition();
  }

  checkScrollPosition(): void {
    // Mostra o botão quando o usuário rolar mais de 300px
    this.showBackToTop = window.pageYOffset > 300;
  }

  scrollToTop(): void {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
}
