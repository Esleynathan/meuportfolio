import { Component, OnInit } from '@angular/core';
import { TranslationService } from '../../services/translation.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  mobileMenuOpen = false;
  isDarkMode = false;
  currentLang: 'pt' | 'en' = 'pt';

  constructor(private translationService: TranslationService) {}

  ngOnInit(): void {
    // Carrega preferências salvas do localStorage
    const savedTheme = localStorage.getItem('theme');

    if (savedTheme === 'dark') {
      this.isDarkMode = true;
      document.documentElement.classList.add('dark');
    }

    // Sincroniza o idioma do navbar com o service
    this.translationService.currentLanguage$.subscribe(lang => {
      this.currentLang = lang;
    });
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
  }
}
