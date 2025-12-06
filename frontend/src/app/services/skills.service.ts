import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, EMPTY } from 'rxjs';
import { expand, reduce, map } from 'rxjs/operators';
import { environment } from '../../environments/environment';
import { Skill } from '../models/skill.model';

interface PaginatedResponse<T> {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}

@Injectable({
  providedIn: 'root'
})
export class SkillsService {
  private apiUrl = `${environment.apiUrl}/skills`;

  constructor(private http: HttpClient) {}

  getSkills(): Observable<Skill[]> {
    // Busca a primeira página e, usando o operador `expand`, continua buscando
    // as próximas páginas (`response.next`) até que não haja mais.
    // O `reduce` acumula os resultados de todas as páginas em um único array.
    return this.http.get<PaginatedResponse<Skill>>(`${this.apiUrl}/`).pipe(
      expand(response => {
        // Se a resposta tiver um campo 'next', faz uma nova requisição para essa URL.
        // Se não, retorna EMPTY para finalizar o fluxo.
        return response.next ? this.http.get<PaginatedResponse<Skill>>(response.next) : EMPTY;
      }),
      // Acumula os 'results' de cada resposta em um único array.
      reduce((acc, response) => acc.concat(response.results), [] as Skill[])
    );
  }

  getSkillsByCategory(category: string): Observable<Skill[]> {
    return this.http.get<PaginatedResponse<Skill>>(`${this.apiUrl}/by-category/?category=${category}`)
      .pipe(map(response => response.results));
  }

  getSkillById(id: number): Observable<Skill> {
    return this.http.get<Skill>(`${this.apiUrl}/${id}/`);
  }
}
