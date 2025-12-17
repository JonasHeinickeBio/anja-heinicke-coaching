# Bilder / Photos

Dieser Ordner ist für Fotos und Bilder, die auf der Website verwendet werden.

## Verwendung

### Bilder hochladen

1. Laden Sie Ihre Bilder in diesen Ordner hoch
2. Empfohlene Formate: JPG, PNG, WebP
3. Empfohlene Optimierung: Komprimieren Sie Bilder vor dem Upload

### Bilder in Markdown-Seiten einbinden

In Ihren `.md` Dateien können Sie Bilder wie folgt einbinden:

```markdown
![Bildbeschreibung]({{ '/assets/images/dateiname.jpg' | relative_url }})
```

### Beispiele

```markdown
# Bild mit Beschreibung
![Retreat in der Toskana]({{ '/assets/images/toskana-landschaft.jpg' | relative_url }})

# Bild mit Link
[![Anja Heinicke]({{ '/assets/images/portrait.jpg' | relative_url }})]({{ '/about/' | relative_url }})
```

### Im Layout oder HTML verwenden

```html
<img src="{{ '/assets/images/hero-background.jpg' | relative_url }}" alt="Beschreibung">
```

## Ordnerstruktur

Sie können auch Unterordner erstellen für bessere Organisation:

```
assets/images/
├── retreat/          # Retreat-Fotos
│   ├── toskana-1.jpg
│   └── toskana-2.jpg
├── portraits/        # Portraitfotos
│   └── anja.jpg
└── nature/          # Naturfotos
    ├── landscape-1.jpg
    └── landscape-2.jpg
```

Dann einbinden mit:
```markdown
![Retreat]({{ '/assets/images/retreat/toskana-1.jpg' | relative_url }})
```

## Best Practices

1. **Dateinamen**: Verwenden Sie beschreibende Namen ohne Leerzeichen (z.B. `toskana-retreat-2024.jpg`)
2. **Größe**: Optimieren Sie Bilder für Web (max. 1920px Breite für große Bilder)
3. **Format**: JPG für Fotos, PNG für Grafiken mit Transparenz
4. **Alt-Text**: Immer einen beschreibenden Alt-Text angeben für Barrierefreiheit

## Bildoptimierung

Online-Tools zur Bildoptimierung:
- [TinyPNG](https://tinypng.com/) - JPG/PNG Komprimierung
- [Squoosh](https://squoosh.app/) - Moderne Bildoptimierung
- [ImageOptim](https://imageoptim.com/) - Desktop-Tool (Mac)
