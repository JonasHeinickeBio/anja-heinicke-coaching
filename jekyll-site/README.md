# Jekyll Site für Anja Heinicke Coaching

Dieser Ordner enthält die Jekyll-basierte Version der Website mit strukturierten Markdown-Dateien und Layouts.

## Was ist Jekyll?

Jekyll ist ein Static Site Generator, der Markdown- und HTML-Dateien mit YAML-Frontmatter in eine komplette statische Website umwandelt. Die Hauptvorteile sind:

- **Strukturierte Inhalte**: Markdown-Dateien sind einfach zu bearbeiten
- **Wiederverwendbare Layouts**: Ein Layout für alle Seiten
- **GitHub Pages Integration**: Automatisches Bauen und Deployen
- **Erweiterbarkeit**: Collections für Blog-Posts oder weitere Inhalte

## Struktur

```
jekyll-site/
├── _config.yml              # Site-Konfiguration (Titel, URL, Metadaten)
├── _layouts/                # Layout-Templates
│   └── default.html         # Grundlayout mit Navigation und Footer
├── assets/                  # Statische Assets
│   ├── css/
│   │   └── style.css        # Stylesheet
│   └── images/              # Bilder und Fotos für die Website
│       ├── README.md        # Anleitung zur Bildverwendung
│       └── .gitkeep         # Stellt sicher, dass der Ordner verfolgt wird
├── index.md                 # Startseite (Hero, Angebot, Themen)
├── retreat.md               # Details zum 5-Tage Retreat in der Toskana
├── about.md                 # Über mich (Therapeutin, Supervisorin, Coach)
├── kontakt.md               # Kontaktseite mit Vorgespräch-Infos
└── README.md                # Diese Datei
```

## YAML Frontmatter

Jede Markdown-Seite beginnt mit YAML Frontmatter:

```yaml
---
layout: default
title: "Seitentitel"
description: "Seitenbeschreibung für SEO"
permalink: /seite/
---
```

### Frontmatter-Felder:

- **layout**: Welches Layout verwendet werden soll (z.B. `default`)
- **title**: Titel der Seite (erscheint im Browser-Tab)
- **description**: Meta-Description für Suchmaschinen
- **permalink**: URL-Pfad der Seite (z.B. `/retreat/`)

## GitHub Pages Deployment

### GitHub Actions (Empfohlen) ✅

Die Site verwendet GitHub Actions für automatisches Deployment. Der Workflow ist bereits konfiguriert in `.github/workflows/jekyll.yml`.

**Setup:**
1. Gehe zu Repository Settings → Pages
2. Wähle unter "Source": **GitHub Actions**
3. Bei jedem Push auf `main` wird die Site automatisch gebaut und deployed

Der Workflow:
- Baut die Jekyll-Site aus dem `jekyll-site/` Ordner
- Installiert automatisch alle Dependencies
- Deployed zu GitHub Pages

### Alternative Optionen

#### Option 1: Root-Verzeichnis
Wenn die Jekyll-Dateien im Hauptverzeichnis liegen, werden sie automatisch gebaut.

#### Option 2: Docs-Ordner
Alternativ kann GitHub Pages so konfiguriert werden, dass es einen `/docs` Ordner verwendet.

#### Option 3: Jekyll-Site Unterordner
Um die Jekyll-Site aus diesem Unterordner zu deployen:

1. Kopiere den Inhalt von `jekyll-site/` ins Hauptverzeichnis, oder
2. Konfiguriere GitHub Pages, um aus einem Branch zu bauen

## Lokale Entwicklung

Um die Site lokal zu testen:

```bash
# Jekyll installieren (einmalig)
gem install jekyll bundler

# In das jekyll-site Verzeichnis wechseln
cd jekyll-site

# Gemfile erstellen (optional, für bessere Dependency-Verwaltung)
bundle init
bundle add jekyll

# Site bauen und Server starten
jekyll serve

# Site ist dann verfügbar unter: http://localhost:4000
```

## Seiten bearbeiten

Die Markdown-Dateien können direkt in GitHub oder lokal bearbeitet werden:

1. **index.md**: Startseite mit Hero-Section, Angebot und Themen
2. **retreat.md**: Detaillierte Beschreibung des 5-Tage-Retreats
3. **about.md**: Informationen über Anja Heinicke und ihre Arbeitsweise
4. **kontakt.md**: Kontaktinformationen und FAQ

## Bilder hinzufügen

### Bilder hochladen

1. Laden Sie Ihre Fotos in den Ordner `assets/images/` hoch
2. Empfohlene Formate: JPG, PNG, WebP
3. Verwenden Sie beschreibende Dateinamen ohne Leerzeichen (z.B. `toskana-retreat.jpg`)

### Bilder in Seiten einbinden

In Markdown-Dateien:

```markdown
![Bildbeschreibung]({{ '/assets/images/dateiname.jpg' | relative_url }})
```

In HTML:

```html
<img src="{{ '/assets/images/dateiname.jpg' | relative_url }}" alt="Bildbeschreibung">
```

Siehe `assets/images/README.md` für weitere Details und Best Practices.

## Zukünftige Erweiterungen

### Blog/Artikel hinzufügen

Collections können für Blog-Posts aktiviert werden. In `_config.yml`:

```yaml
collections:
  posts:
    output: true
    permalink: /blog/:title/
```

Dann Posts in `_posts/` erstellen mit dem Format: `YYYY-MM-DD-titel.md`

### Weitere Seiten

Neue Seiten einfach als `.md` Dateien im Hauptverzeichnis erstellen mit entsprechendem Frontmatter.

### Includes

Für wiederverwendbare Komponenten können Includes in `_includes/` erstellt werden:

```
_includes/
├── header.html
├── footer.html
└── testimonial.html
```

Diese dann mit `{% include header.html %}` einbinden.

## Anpassungen

### CSS anpassen
Die Stylesheet-Datei liegt in `assets/css/style.css` und kann direkt bearbeitet werden.

### Navigation ändern
Die Navigation ist im `_layouts/default.html` Template definiert und kann dort angepasst werden.

### Metadaten ändern
Site-weite Einstellungen werden in `_config.yml` vorgenommen.

## Weitere Ressourcen

- [Jekyll Dokumentation](https://jekyllrb.com/docs/)
- [GitHub Pages + Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll)
- [Liquid Template Language](https://shopify.github.io/liquid/)
- [YAML Frontmatter](https://jekyllrb.com/docs/front-matter/)
