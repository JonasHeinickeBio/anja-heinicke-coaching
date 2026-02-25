# anja-heinicke-coaching
Systemische Coach mit Schwerpunkt auf Coaching in der Natur und Kleinstgruppen-Retreats. Ich begleite Menschen bei Burnout, Selfcare, Grenzen ziehen und Neuorientierung. Neben online Einzelcoachings biete ich 5-tägige Retreats in einem kleinen toskanischen Dorf an.

## HTML Structure Standards

This website follows modern HTML5 semantic structure and accessibility best practices:

### Semantic HTML Structure
All pages use consistent semantic HTML5 elements:
- `<nav>` with `role="navigation"` and `aria-label="Hauptnavigation"` for main navigation
- `<main>` wrapper around primary page content (all sections)
- `<section>` elements with unique IDs for different content areas
- `<footer>` with consistent structure across all pages
- Proper heading hierarchy (h1 → h2 → h3 → h4)

### Page Structure Template
```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="[Page Description]">
    <title>[Page Title] - Anja Heinicke Coaching</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <nav class="navigation" role="navigation" aria-label="Hauptnavigation">
        <!-- Navigation content -->
    </nav>

    <main>
        <!-- Page sections -->
    </main>

    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <!-- Footer content -->
            </div>
        </div>
    </footer>

    <script src="assets/js/main.js"></script>
</body>
</html>
```

### CSS Component Library
The website uses a consistent component library defined in `assets/css/style.css`:
- **CSS Custom Properties**: Centralized design tokens for colors, spacing, shadows, etc.
- **Layout Components**: `.container`, `.section`, `.section-alt`
- **UI Components**: `.btn`, `.card`, `.badge`
- **Utility Classes**: Spacing, flexbox, text alignment utilities

### JavaScript
All interactive functionality is centralized in `assets/js/main.js`:
- Smooth scrolling for anchor links
- Navigation scroll effects
- Active link highlighting
- Intersection Observer for fade-in animations

### Accessibility Features
- ARIA labels on navigation elements
- Proper heading hierarchy on all pages
- Descriptive alt text for images
- Keyboard-accessible navigation
- Focus states on interactive elements

### File Structure
```
/
├── index.html           # Homepage
├── about.html           # About page
├── offer.html           # Services overview
├── online-coaching.html # Online coaching details
├── retreat.html         # Retreat information
├── topics.html          # Coaching topics
├── contact.html         # Contact page
├── impressum.html       # Legal notice
├── assets/
│   ├── css/
│   │   └── style.css    # Main stylesheet
│   ├── js/
│   │   └── main.js      # Main JavaScript
│   └── images/          # Image assets
└── README.md
```

## Development

This is a static website with no build process required. Simply open any HTML file in a browser to view locally, or use a local server:

```bash
python3 -m http.server 8080
```

Then navigate to `http://localhost:8080` in your browser.

