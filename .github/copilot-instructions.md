## Repo snapshot & purpose

This repo contains two parallel website sources: a single-page HTML site in the repository root (`index.html`, `style.css`) and a structured Jekyll site in `jekyll-site/` (preferred for ongoing content work). The Jekyll site is intended for GitHub Pages and is wired to GitHub Actions.

## High-level architecture

- Root static site: `index.html`, `style.css` — a standalone landing page used previously.
- Jekyll site: `jekyll-site/` — Markdown pages (`index.md`, `about.md`, `retreat.md`, `kontakt.md`), layouts in `_layouts/` (see `jekyll-site/_layouts/default.html`), and assets in `jekyll-site/assets/`.
- CI: `.github/workflows/jekyll-test.yml` (build on PRs/branches) and `.github/workflows/jekyll-deploy.yml` (deploy on `main`).

When making content or structure edits, prefer the `jekyll-site/` tree unless a deliberate migration to the root is required. The `JEKYLL_STRUCTURE.md` file documents the intended workflow and deployment behavior.

## Developer workflows (concrete commands)

- Local Jekyll development (from repo root):

  cd jekyll-site
  gem install jekyll bundler   # one-time
  bundle install
  bundle exec jekyll serve    # serves at http://localhost:4000

- Build verification in CI: GitHub Actions already runs a test build for branches/PRs (see `.github/workflows/jekyll-test.yml`). Push to `main` triggers the deploy workflow.

## Project-specific conventions & patterns

- Two-site coexistence: do NOT edit both `index.html` (root) and the pages in `jekyll-site/` for the same content — this causes duplication and drift. The canonical source is `jekyll-site/`.
- Navigation is defined in `jekyll-site/_layouts/default.html`. Update links and menus there (Liquid `relative_url` is used).
- Images live under `jekyll-site/assets/images/` and are referenced with Liquid, e.g. `{{ '/assets/images/toskana-landschaft.jpg' | relative_url }}`.
- CSS lives at `jekyll-site/assets/css/style.css` (copy of root `style.css`). Edit the Jekyll copy for the site served by GH Pages.

## How to add or modify content (quick examples)

- Add a page: create `jekyll-site/preise.md` with YAML front matter:

  ---
  layout: default
  title: "Preise"
  permalink: /preise/
  ---

  Then add the page body in Markdown below the front matter and commit.

- Add an image: upload to `jekyll-site/assets/images/retreat/` and reference in markdown:

  ![Alt text]({{ '/assets/images/retreat/photo.jpg' | relative_url }})

## CI / Deployment notes (non-obvious)

- Deploy happens only on `main` via `.github/workflows/jekyll-deploy.yml`. PRs and other branches only run a build check (`jekyll-test.yml`). Keep the deploy-safe changes gated to `main`.
- If you change Ruby gems or `Gemfile`, ensure the deploy workflow still installs dependencies (see `jekyll-deploy.yml`). Local `bundle install` mirrors CI behavior.

## Files to check for common edits

- Content & pages: `jekyll-site/*.md` (index.md, about.md, retreat.md, kontakt.md)
- Layouts & navigation: `jekyll-site/_layouts/default.html`
- Site config: `jekyll-site/_config.yml` (title, lang, markdown engine, exclusions)
- Assets: `jekyll-site/assets/css/style.css`, `jekyll-site/assets/images/`
- CI: `.github/workflows/jekyll-test.yml`, `.github/workflows/jekyll-deploy.yml`

## Small gotchas for automated agents

- Prefer editing `jekyll-site/` unless the task explicitly targets the root single-file site. If asked to change copy/site-wide templates, update the Jekyll layout and the Markdown pages.
- Keep commits small and focused: content change vs layout vs assets should be separate PRs so CI results are easy to interpret.
- Use `relative_url` when creating internal links so the site works with `baseurl` left empty or when deployed under a path.

## If unsure — ask these targeted questions

- Should the change apply to the legacy root site or the canonical `jekyll-site/`? (default: `jekyll-site/`)
- Is this a content, layout, or asset change? (helps split PRs)
- Will this require updating `Gemfile` / CI workflows? (if yes, run CI and ensure deploy workflow still succeeds)

---
If any of this doesn't match your intent, tell me which site is canonical (root `index.html` vs `jekyll-site/`) and I will adjust the instructions and update the file accordingly.
