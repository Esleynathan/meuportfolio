import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ContactService } from '../../services/contact.service';
import { TranslationService } from '../../services/translation.service';

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.css']
})
export class ContactComponent implements OnInit {
  contactForm!: FormGroup;
  isSubmitting = false;
  submitSuccess = false;
  submitError: string | null = null;

  constructor(
    private fb: FormBuilder,
    private contactService: ContactService,
    private translationService: TranslationService
  ) {}

  ngOnInit(): void {
    this.contactForm = this.fb.group({
      name: ['', [Validators.required, Validators.minLength(3)]],
      email: ['', [Validators.required, Validators.email]],
      subject: ['', [Validators.required, Validators.minLength(5)]],
      message: ['', [Validators.required, Validators.minLength(10)]]
    });
  }

  onSubmit(): void {
    if (this.contactForm.invalid) {
      this.contactForm.markAllAsTouched();
      return;
    }

    this.isSubmitting = true;
    this.submitSuccess = false;
    this.submitError = null;

    this.contactService.sendMessage(this.contactForm.value).subscribe({
      next: (response) => {
        this.submitSuccess = true;
        this.isSubmitting = false;
        this.contactForm.reset();

        // Remove mensagem de sucesso após 5 segundos
        setTimeout(() => {
          this.submitSuccess = false;
        }, 5000);
      },
      error: (err) => {
        this.submitError = this.translationService.translate('contact.error');
        this.isSubmitting = false;
        console.error('Erro ao enviar mensagem:', err);
      }
    });
  }

  // Helper methods para validação no template
  isFieldInvalid(fieldName: string): boolean {
    const field = this.contactForm.get(fieldName);
    return !!(field && field.invalid && field.touched);
  }

  getFieldError(fieldName: string): string {
    const field = this.contactForm.get(fieldName);
    if (!field || !field.errors) return '';

    if (field.errors['required']) {
      return this.translationService.translate('contact.required');
    }
    if (field.errors['email']) {
      return this.translationService.translate('contact.invalidEmail');
    }
    if (field.errors['minlength']) {
      const minLength = field.errors['minlength'].requiredLength;
      const template = this.translationService.translate('contact.minLength');
      return template.replace('{min}', minLength.toString());
    }
    return '';
  }
}
