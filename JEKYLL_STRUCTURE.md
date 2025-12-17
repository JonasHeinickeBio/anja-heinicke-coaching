# Jekyll Struktur - Übersicht

## Überblick

Dieses Repository enthält nun **zwei Versionen** der Website:

1. **Ursprüngliche Version** (im Hauptverzeichnis):
   - `index.html` - Single-Page HTML Website
   - `style.css` - Stylesheet
   - `README.md` - Repository-Beschreibung

2. **Jekyll Version** (im `jekyll-site/` Unterordner):
   - Strukturierte Multi-Page Website mit Jekyll
   - Markdown-Dateien mit YAML Frontmatter
   - Wiederverwendbare Layouts
   - Bereit für GitHub Pages

## Warum Jekyll?

Jekyll ist ein Static Site Generator, der besonders nützlich ist für:

- ✅ **Strukturierte Inhalte**: Einfach zu bearbeitende Markdown-Dateien
- ✅ **Mehrere Seiten**: Klare Trennung verschiedener Inhaltsbereiche
- ✅ **Wiederverwendbare Templates**: Ein Layout für alle Seiten
- ✅ **GitHub Pages Integration**: Automatisches Bauen und Deployen
- ✅ **Skalierbarkeit**: Einfach neue Seiten oder Blog-Posts hinzufügen

## Jekyll Site Struktur

```
jekyll-site/
├── _config.yml              # Konfiguration (Titel, URL, Autor, etc.)
├── _layouts/                # Layout-Templates
│   └── default.html         # Hauptlayout mit Navigation & Footer
├── assets/                  # Statische Ressourcen
│   └── css/
│       └── style.css        # Stylesheet (Kopie vom Original)
├── index.md                 # Startseite mit Hero & Übersicht
├── retreat.md               # Retreat-Details (5-Tage Programm)
├── about.md                 # Über mich Seite
├── kontakt.md               # Kontaktseite
├── Gemfile                  # Ruby Dependencies
└── README.md                # Dokumentation
```

## Seiten-Übersicht

### 1. index.md - Startseite
**Permalink**: `/`
**Inhalt**:
- Hero Section mit Hauptbotschaft
- Einleitung zu Coaching Retreats
- Das Angebot (Klein & Persönlich, Natur als Therapeutin)
- Coaching Themen (Burnout, Self-Care, Grenzen, etc.)
- Erfahrungsbericht
- Call-to-Action

### 2. retreat.md - Retreat Details
**Permalink**: `/retreat/`
**Inhalt**:
- Setting in der Toskana
- Detaillierter 5-Tage Ablauf
- Tag 1: Ankommen
- Tage 2-4: Kernprogramm mit Zeitplan
- Tag 5: Abschluss
- Zusätzliche Angebote
- Was Sie erwartet

### 3. about.md - Über mich
**Permalink**: `/about/`
**Inhalt**:
- Vorstellung als Systemische Therapeutin, Supervisorin & Coach
- Grundhaltung und Arbeitsweise
- Die Frage nach dem "Statt dessen"
- Mein Angebot (Einzelcoaching, Retreats, Wartezeit-Begleitung)
- Spezialisierung
- Erfahrungsbericht
- Call-to-Action für Vorgespräch

### 4. kontakt.md - Kontakt
**Permalink**: `/kontakt/`
**Inhalt**:
- Kontaktinformationen (E-Mail)
- Vorgespräch vereinbaren
- Häufige Fragen (FAQ)
- Standort-Informationen
- Call-to-Action

## YAML Frontmatter

Jede Seite verwendet YAML Frontmatter zur Konfiguration:

```yaml
---
layout: default           # Welches Layout verwendet wird
title: "Seitentitel"      # Erscheint im Browser-Tab
description: "..."        # Meta-Description für SEO
permalink: /pfad/         # URL der Seite
---
```

## GitHub Pages Deployment

### Option 1: Aus dem Root-Verzeichnis deployen

1. Kopiere den Inhalt von `jekyll-site/` ins Hauptverzeichnis
2. GitHub Pages baut die Site automatisch

```bash
# Von der Kommandozeile:
cp -r jekyll-site/* .
git add .
git commit -m "Deploy Jekyll site"
git push
```

### Option 2: Aus einem Unterordner deployen

GitHub Pages kann so konfiguriert werden, dass es aus dem `/docs` Ordner baut:

1. Benenne `jekyll-site/` in `docs/` um
2. In GitHub: Settings → Pages → Source → "docs" folder wählen

### Option 3: Mit GitHub Actions

Erstelle `.github/workflows/jekyll.yml` für custom Build-Prozess.

## Lokale Entwicklung

Um die Jekyll-Site lokal zu testen:

```bash
# Jekyll installieren (einmalig)
gem install jekyll bundler

# In das jekyll-site Verzeichnis wechseln
cd jekyll-site

# Dependencies installieren
bundle install

# Site bauen und Server starten
bundle exec jekyll serve

# Alternativ:
jekyll serve
```

Die Site ist dann verfügbar unter: `http://localhost:4000`

## Inhalte bearbeiten

### Eine Seite bearbeiten

1. Öffne die entsprechende `.md` Datei (z.B. `about.md`)
2. Bearbeite den Markdown-Inhalt unterhalb des Frontmatters
3. Speichern und committen

### Neue Seite hinzufügen

1. Erstelle eine neue `.md` Datei (z.B. `preise.md`)
2. Füge YAML Frontmatter hinzu:
   ```yaml
   ---
   layout: default
   title: "Preise"
   permalink: /preise/
   ---
   ```
3. Füge den Inhalt in Markdown hinzu
4. Aktualisiere die Navigation in `_layouts/default.html`

### Blog/Artikel hinzufügen

Um einen Blog hinzuzufügen:

1. Aktiviere Collections in `_config.yml`:
   ```yaml
   collections:
     posts:
       output: true
       permalink: /blog/:title/
   ```

2. Erstelle Ordner `_posts/`

3. Erstelle Posts mit Format: `YYYY-MM-DD-titel.md`
   ```yaml
   ---
   layout: default
   title: "Artikel-Titel"
   date: 2024-01-15
   ---
   ```

## CSS anpassen

Das Stylesheet liegt in `assets/css/style.css` und ist eine Kopie des Originals. Änderungen können direkt vorgenommen werden.

## Navigation anpassen

Die Navigation ist im Layout-Template definiert (`_layouts/default.html`):

```html
<nav class="navigation">
    <ul>
        <li><a href="{{ '/' | relative_url }}">Home</a></li>
        <li><a href="{{ '/about/' | relative_url }}">Über mich</a></li>
        <li><a href="{{ '/retreat/' | relative_url }}">Retreat</a></li>
        <li><a href="{{ '/kontakt/' | relative_url }}">Kontakt</a></li>
    </ul>
</nav>
```

## Vorteile der Jekyll-Struktur

1. **Wartbarkeit**: Inhalte sind in separate Dateien aufgeteilt
2. **SEO**: Jede Seite hat eigene URL, Title und Description
3. **Skalierbarkeit**: Einfach neue Seiten hinzufügen
4. **Content Management**: Markdown ist einfacher zu bearbeiten als HTML
5. **Konsistenz**: Ein Layout für alle Seiten
6. **GitHub Integration**: Automatisches Deployment zu GitHub Pages

## Nächste Schritte

1. **Testen**: Lokale Installation und Test mit `jekyll serve`
2. **Deployment**: Wähle eine Deployment-Option (siehe oben)
3. **Erweiterungen**: 
   - Blog-Funktionalität hinzufügen
   - Weitere Seiten erstellen (z.B. Preise, Termine)
   - Jekyll-Plugins hinzufügen (SEO, Sitemap, etc.)

## Ressourcen

- [Jekyll Dokumentation](https://jekyllrb.com/docs/)
- [GitHub Pages + Jekyll Guide](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll)
- [Markdown Syntax](https://www.markdownguide.org/basic-syntax/)
- [YAML Frontmatter](https://jekyllrb.com/docs/front-matter/)
- [Liquid Template Language](https://shopify.github.io/liquid/)

## Support

Bei Fragen zur Jekyll-Struktur siehe:
- `jekyll-site/README.md` für technische Details
- Jekyll Community Forum
- GitHub Pages Dokumentation
