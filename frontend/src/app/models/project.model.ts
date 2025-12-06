export interface Project {
  id: number;
  title: string;
  slug: string;
  description: string;
  detailed_description: string;
  technologies: string;
  github_url: string;
  live_url?: string;
  image?: string;
  featured: boolean;
  order: number;
  created_at: string;
  updated_at: string;
}
