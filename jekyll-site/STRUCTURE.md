# Jekyll Site Structure - Clean Content Architecture

Diese Jekyll-Site folgt Best Practices für die Trennung von Inhalt und Layout.

## Prinzipien

### 1. Content in Markdown
- Seiten-Inhalte sind primär in **Markdown** geschrieben
- Minimale HTML-Strukturen nur wo nötig (Sections für Styling)
- Fokus auf Lesbarkeit und einfache Bearbeitbarkeit

### 2. Layout in Templates
- HTML-Struktur lebt in `_layouts/default.html`
- Wiederverwendbare Komponenten in `_includes/`
- CSS bleibt in separaten Dateien

### 3. Klare Dateiorganisation
```
jekyll-site/
├── _config.yml              # Site-Konfiguration
├── _layouts/
│   └── default.html         # Basis-Layout (Navigation, Footer)
├── _includes/
│   ├── hero.html            # Hero-Section Component
│   └── section.html         # Wiederverwendbare Section (optional)
├── assets/
│   ├── css/style.css
│   └── images/
├── index.md                 # Startseite (root-level)
├── about.md                 # Über mich
├── retreat.md               # Retreat-Details
└── kontakt.md               # Kontakt

KEINE pages/ Unterordner mehr - Seiten liegen direkt im Root!
```

## Seiten-Anatomie

### Frontmatter (YAML)
Jede Seite beginnt mit Metadaten:

```yaml
---
layout: default
title: "Seitentitel"
description: "SEO-Description"
permalink: /pfad/
---
```

### Content (Markdown)
Nach dem Frontmatter folgt der Inhalt in Markdown:

```markdown
<section class="section">
<div class="container" markdown="1">

## Überschrift

**Fetter Text** für Betonung.

- Liste
- von
- Punkten

</div>
</section>
```

**Wichtig:** `markdown="1"` innerhalb von HTML-Elementen aktiviert Markdown-Verarbeitung!

## Includes verwenden

### Hero-Section Include
```liquid
{% include hero.html 
  title="Hauptüberschrift" 
  subtitle="Untertitel"
  tagline="Kurzer Aufhänger"
  description="Längere Beschreibung"
  cta_text="Button-Text"
  cta_link="#ziel"
%}
```

### Manuelle Sections
Für volle Kontrolle können Sections auch manuell geschrieben werden:

```markdown
<section id="meine-section" class="section section-alt">
<div class="container" markdown="1">

## Meine Überschrift

Content hier in Markdown...

</div>
</section>
```

## CSS-Klassen

### Section-Typen
- `.section` - Standard Section mit weißem Hintergrund
- `.section-alt` - Alternative Section mit anderem Hintergrund

### Content-Boxen
- `.content-box` - Standard Content-Container
- `.retreat-details` - Grid-Layout für Detail-Karten
- `.detail-item` - Einzelne Karte/Detail
- `.testimonial` - Styling für Testimonials

### Hervorhebungen
- `.lead` - Größerer Lead-Text
- `.hero-subtitle` - Subtitle-Text im Hero
- `.cta-button` - Call-to-Action Button

## Markdown-Syntax Übersicht

```markdown
# H1 Überschrift
## H2 Überschrift
### H3 Überschrift

**Fett** und *kursiv*

- Ungeordnete
- Liste

1. Nummerierte
2. Liste

[Link-Text](url)

> Blockquote

`Code inline`
```

## Best Practices

### ✅ DO

1. **Content in Markdown schreiben**
   ```markdown
   ## Überschrift
   
   Normaler Text mit **Betonung**.
   ```

2. **Semantische HTML-Struktur beibehalten**
   ```html
   <section class="section">
   <div class="container" markdown="1">
   ... Markdown content ...
   </div>
   </section>
   ```

3. **Includes für wiederholte Patterns**
   ```liquid
   {% include hero.html ... %}
   ```

4. **Site-Variablen nutzen**
   ```liquid
   {{ site.author.email }}
   {{ site.title }}
   ```

### ❌ DON'T

1. **Keine komplexen HTML-Strukturen im Content**
   ```html
   <!-- NICHT SO: -->
   <div class="detail-item">
     <h3>Titel</h3>
     <p>Text</p>
   </div>
   
   <!-- BESSER: -->
   ### Titel
   Text
   ```

2. **Keine inline Styles**
   ```html
   <!-- NICHT SO: -->
   <p style="color: red;">Text</p>
   
   <!-- BESSER: -->
   <p class="highlight">Text</p>
   ```

3. **Keine duplizierte Navigation/Footer im Content**
   Das gehört in `_layouts/default.html`!

## Neue Seite hinzufügen

1. Neue Datei erstellen: `jekyll-site/meine-seite.md`

2. Frontmatter hinzufügen:
   ```yaml
   ---
   layout: default
   title: "Meine Seite"
   description: "Beschreibung für SEO"
   permalink: /meine-seite/
   ---
   ```

3. Content in Markdown schreiben

4. Navigation aktualisieren in `_layouts/default.html`:
   ```html
   <li><a href="{{ '/meine-seite/' | relative_url }}">Meine Seite</a></li>
   ```

## Test Workflow Validierung

Der Test-Workflow prüft automatisch:

✅ Jekyll Build erfolgreich  
✅ Alle Seiten generiert (index, about, retreat, kontakt)  
✅ HTML-Validierung (DOCTYPE, title, meta description)  
✅ Navigation vorhanden  
✅ Deutsche Sprache gesetzt (`lang="de"`)  
✅ Links nicht gebrochen  
✅ Screenshots erstellt

Alle Änderungen müssen diese Tests bestehen!

## Weitere Informationen

- **Jekyll Docs:** https://jekyllrb.com/docs/
- **Kramdown Syntax:** https://kramdown.gettalong.org/syntax.html
- **Liquid Templating:** https://shopify.github.io/liquid/

## Support

Bei Fragen zur Struktur oder Markdown-Konvertierung siehe:
- `README.md` für technische Details
- `JEKYLL_STRUCTURE.md` für Deployment-Optionen
