import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
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
    return this.http.get<PaginatedResponse<Skill>>(`${this.apiUrl}/`)
      .pipe(map(response => response.results));
  }

  getSkillsByCategory(category: string): Observable<Skill[]> {
    return this.http.get<PaginatedResponse<Skill>>(`${this.apiUrl}/by-category/?category=${category}`)
      .pipe(map(response => response.results));
  }

  getSkillById(id: number): Observable<Skill> {
    return this.http.get<Skill>(`${this.apiUrl}/${id}/`);
  }
}
