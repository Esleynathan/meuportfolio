import { Component, HostListener } from '@angular/core';

@Component({
  selector: 'app-hero',
  templateUrl: './hero.component.html',
  styleUrls: ['./hero.component.css']
})
export class HeroComponent {

  // ... outras propriedades existentes ...
  isAtTop = true;

  @HostListener('window:scroll', [])
  onWindowScroll(): void {
    // A seta desaparecerá quando o usuário rolar mais de 50% da altura da tela,
    // que é um bom ponto para sincronizar com o aparecimento do botão "Voltar ao Topo".
    this.isAtTop = window.scrollY < (window.innerHeight / 2);
  }
  // ... resto do componente ...
}
