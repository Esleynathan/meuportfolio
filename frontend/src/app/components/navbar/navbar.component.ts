import {
  Component,
  OnInit,
  AfterViewInit,
  ElementRef,
  HostListener,
} from '@angular/core';
import { TranslationService } from '../../services/translation.service';

// Declara a variável global Headroom para que o TypeScript a reconheça.
declare var Headroom: any;

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css'],
})
export class NavbarComponent implements OnInit, AfterViewInit {
  mobileMenuOpen = false;
  isDarkMode = false;
  currentLang: 'pt' | 'en' = 'pt';
  isScrolled = false;

  constructor(
    public translationService: TranslationService,
    private elementRef: ElementRef
  ) {}

  ngOnInit(): void {
    // Carrega preferências salvas do localStorage
    const savedTheme = localStorage.getItem('theme');
    this.isScrolled = window.scrollY > 10;

    // Define dark mode como padrão se não houver preferência salva
    if (savedTheme === 'light') {
      this.isDarkMode = false;
      document.documentElement.classList.remove('dark');
    } else {
      // Dark mode por padrão (quando não há preferência ou quando é 'dark')
      this.isDarkMode = true;
      document.documentElement.classList.add('dark');
      // Salva a preferência padrão se ainda não existir
      if (!savedTheme) {
        localStorage.setItem('theme', 'dark');
      }
    }

    // Sincroniza o idioma do navbar com o service
    this.translationService.currentLanguage$.subscribe(lang => {
      this.currentLang = lang;
    });
  }

  ngAfterViewInit(): void {
    // Pega o elemento <nav> dentro do template do componente
    const navbarElement = this.elementRef.nativeElement.querySelector('nav');

    if (navbarElement) {
      // Inicializa o Headroom.js no elemento da navbar
      const headroom = new Headroom(navbarElement, {
        offset: 200, // Distância em pixels que o usuário deve rolar antes do headroom agir
        tolerance: 5, // Tolerância para evitar ativação em pequenos scrolls
        classes: {
          initial: 'headroom',
          pinned: 'headroom--pinned',
          unpinned: 'headroom--unpinned',
          top: 'headroom--top',
          notTop: 'headroom--not-top',
          bottom: 'headroom--bottom',
          notBottom: 'headroom--not-bottom',
        },
      });
      headroom.init();
    }
  }

  toggleMobileMenu() {
    this.mobileMenuOpen = !this.mobileMenuOpen;
  }

  closeMobileMenu() {
    this.mobileMenuOpen = false;
  }

  toggleDarkMode() {
    this.isDarkMode = !this.isDarkMode;

    if (this.isDarkMode) {
      document.documentElement.classList.add('dark');
      localStorage.setItem('theme', 'dark');
    } else {
      document.documentElement.classList.remove('dark');
      localStorage.setItem('theme', 'light');
    }
  }

  toggleLanguage() {
    const newLang = this.currentLang === 'pt' ? 'en' : 'pt';
    this.translationService.setLanguage(newLang);
    this.closeMobileMenu();
  }

  @HostListener('window:scroll', [])
  onWindowScroll(): void {
    this.isScrolled = window.scrollY > 10;
    if (this.mobileMenuOpen) {
      this.closeMobileMenu();
    }
  }
}
