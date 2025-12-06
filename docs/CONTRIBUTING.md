# Guia de Contribuição e Desenvolvimento

Este documento fornece diretrizes para o desenvolvimento e manutenção do projeto.

## Fluxo de Trabalho (Git Workflow)

Utilizamos um fluxo simplificado baseado no GitHub Flow.

1.  **Branch `main`**: É a branch principal e deve sempre estar em estado de deploy. Ninguém faz push direto para a `main`.
2.  **Feature Branches**: Para cada nova funcionalidade ou correção, crie uma nova branch a partir da `main`.
    - **Nomenclatura**: Use o prefixo `feat/`, `fix/`, `docs/`, `refactor/` seguido por uma descrição curta.
    - Exemplo: `feat/add-lazy-loading` ou `fix/contact-form-validation`.
3.  **Pull Requests (PRs)**: Após concluir o desenvolvimento na sua branch, abra um Pull Request para a `main`.
    - Descreva o que foi feito no PR.
    - Se houver uma tarefa no `STATUS.md`, referencie-a.
4.  **Code Review**: O PR será revisado (neste caso, por você ou pela IA).
5.  **Merge**: Após a aprovação, o PR é "squashed and merged" na `main`.

## Padrões de Código

### Geral
- **Linguagem**: O código e os comentários devem ser escritos em **Português (Brasil)** para manter a consistência do projeto.
- **Formatação**: Utilize as ferramentas de formatação padrão de cada ecossistema.

### Backend (Python/Django)
- **Formatter**: `black`
- **Linter**: `flake8`
- **Padrão**: Siga a PEP 8.

### Frontend (TypeScript/Angular)
- **Formatter**: `prettier`
- **Linter**: `eslint`
- **Padrão**: Siga o guia de estilo oficial do Angular.

## Mensagens de Commit

Siga o padrão Conventional Commits.
- `feat:` (nova funcionalidade)
- `fix:` (correção de bug)
- `docs:` (mudanças na documentação)
- `style:` (formatação, ponto e vírgula, etc.)
- `refactor:` (refatoração de código sem alteração de funcionalidade)
- `test:` (adição ou refatoração de testes)
- `chore:` (atualização de tarefas de build, pacotes, etc.)

**Exemplo**: `feat(contact): add success message after form submission`