import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TranslationService {
  private currentLang$ = new BehaviorSubject<'pt' | 'en'>('pt');
  private translations: any = {};
  private translationsLoaded = false;

  constructor() {
    this.loadTranslations();
  }

  async loadTranslations(): Promise<void> {
    try {
      // Carregar ambos os arquivos JSON
      const [pt, en] = await Promise.all([
        fetch('/assets/i18n/pt.json').then(r => r.json()),
        fetch('/assets/i18n/en.json').then(r => r.json())
      ]);

      this.translations = { pt, en };
      this.translationsLoaded = true;

      // Carregar idioma salvo do localStorage
      const savedLang = localStorage.getItem('language') as 'pt' | 'en';
      if (savedLang && (savedLang === 'pt' || savedLang === 'en')) {
        this.currentLang$.next(savedLang);
      }
    } catch (error) {
      console.error('Erro ao carregar traduções:', error);
      // Fallback para português
      this.currentLang$.next('pt');
    }
  }

  get currentLanguage$(): Observable<'pt' | 'en'> {
    return this.currentLang$.asObservable();
  }

  get currentLanguage(): 'pt' | 'en' {
    return this.currentLang$.value;
  }

  setLanguage(lang: 'pt' | 'en'): void {
    this.currentLang$.next(lang);
    localStorage.setItem('language', lang);
  }

  translate(key: string): string {
    if (!this.translationsLoaded) {
      return key; // Retorna a chave se traduções ainda não carregaram
    }

    const lang = this.currentLang$.value;
    const keys = key.split('.');
    let value = this.translations[lang];

    // Navega pelo objeto de traduções usando as chaves separadas por ponto
    for (const k of keys) {
      value = value?.[k];
    }

    // Retorna a tradução ou a chave original se não encontrar
    return value || key;
  }
}
