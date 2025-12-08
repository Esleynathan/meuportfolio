import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable, of } from 'rxjs';
import { map, catchError, shareReplay, switchMap, distinctUntilChanged } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class TranslateService {
  private lang$: BehaviorSubject<string>;
  private translations$: Observable<{ [key: string]: any }>;

  constructor(private http: HttpClient) {
    // Detecta o idioma do navegador e define o padrão.
    const browserLang = navigator.language.split('-')[0]; // Extrai 'pt' de 'pt-BR'
    const supportedLangs = ['pt', 'en'];
    const initialLang = supportedLangs.includes(browserLang) ? browserLang : 'en';
    this.lang$ = new BehaviorSubject<string>(initialLang);

    // Cria um observable que reage à mudança de idioma.
    // switchMap cancela a requisição anterior e faz uma nova quando o idioma muda.
    this.translations$ = this.lang$.pipe(
      switchMap(lang =>
        this.http.get<{ [key: string]: any }>(`/assets/i18n/${lang}.json`).pipe(
          catchError(() => of({})) // Em caso de erro, retorna um objeto vazio.
        )
      ),
      shareReplay(1) // Cacheia o último arquivo de tradução carregado.
    );
  }

  /**
   * Altera o idioma ativo da aplicação.
   * @param lang 'en' ou 'pt'
   */
  public use(lang: string): void {
    this.lang$.next(lang);
  }

  public get(key: string): Observable<string> {
    return this.translations$.pipe(
      map(translations => {
        const keys = key.split('.');
        let result = translations;
        for (const k of keys) {
          result = result?.[k];
        }
        // Retorna o resultado apenas se for uma string, senão retorna a chave como fallback.
        return typeof result === 'string' ? result : key;
      }),
      distinctUntilChanged() // Emite um novo valor apenas se a tradução da chave mudar.
    );
  }
}