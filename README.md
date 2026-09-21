# ludovicofurlanetto.github.io (repo: `website`)

Single-page CV site for Ludovico Furlanetto. Plain HTML/CSS/JS, zero
dependencies, no build step. Academic paper styling, single column, hosted
on GitHub Pages.

## Structure

```
website/
├── index.html                  single-page CV
├── css/style.css               academic paper theme + print rules
├── js/main.js                  year, scroll-spy nav, print handling
├── assets/logos/               institution + project logos
│   ├── logo-politecnico-torino.svg
│   ├── logo-sissa.png
│   ├── ictp_logo.png
│   ├── logo-sorbonne.svg
│   ├── logo-paris1.svg
│   ├── logo-unibo.jpeg
│   ├── cargo.png
│   └── logo-backtesto.png      (from backtes.to press assets)
├── cv/ludovico_furlanetto_cv.pdf
├── papers/furlanetto_ludovico_thesis.pdf    M.Sc. thesis (from ~/Documents)
├── papers/furlanetto_ludovico_bs_thesis.pdf B.Sc. thesis (from ~/Documents)
└── README.md
```

## Education entries

The M.Sc. double degree is split into three entries in `index.html`:

- **Politecnico di Torino** — year-1 courses taught at PoliTo
- **SISSA** — year-1 courses taken at SISSA (Advanced Quantum Mechanics & ANM,
  Probability & Information Theory, Introduction to Data Science)
- **Sorbonne Université** — year-2 courses (Statistical Field Theory, Nonlinear
  Physics, Complex Systems, Stochastic Processes)
- **ICTP** — Spring College courses with lecturers (Loureiro & Pastore,
  Mastrogiuseppe, Ciliberto, Zamponi)
- **University of Bologna** — B.Sc. exams

## Logo sources

All logos come from official public sources:

- Politecnico di Torino — official wordmark SVG (Wikimedia `Logo_PoliTo`)
- SISSA — official logo PNG (sissa.it press assets)
- ICTP — official wordmark PNG (diploma.ictp.it)
- Sorbonne Université — official wordmark SVG (Wikimedia `Sorbonne_University_Logo.svg`)
- Université Paris 1 Panthéon-Sorbonne — 2024 official SVG (Wikimedia Commons)
- University of Bologna — official logo JPEG
- Cargo — official Cargo logo PNG (doc.rust-lang.org)

## Courses & professors

Course lists live inline in `index.html` inside `<details class="courses">`
blocks (one per university). They were seeded from the exam transcripts:

- `~/Documents/esami_magistrale_polito.pdf` — M.Sc. course list
- `~/Documents/esami_triennale_unibo.pdf` — B.Sc. course list

Professors in the course tables are filled in. Course names/CFU/SSD can be
corrected the same way.

## Local preview

```sh
python3 -m http.server 8000   # http://localhost:8000
```

## Deploy

For a GitHub Pages **user site** at `https://notludovico.github.io`, the repo
must be named exactly `notludovico.github.io`. Otherwise it deploys as a
**project site** at `https://notludovico.github.io/<repo>/` (asset paths are
relative, so both work without changes).

```sh
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin git@github.com:NotLudovico/<repo>.git
git push -u origin main
```

Then in the repo on GitHub: **Settings → Pages → Source: Deploy from a branch
→ main / (root) → Save**.

Update the CV PDF when it changes:

```sh
cp ~/Documents/ludovico_furlanetto_cv.pdf cv/
```

## Notes

- Printing: the site auto-expands all course lists and drops the top bar
  (view or press Cmd/Ctrl+P).
- The `cv/*.pdf` is a copy; the canonical file stays in `~/Documents/`.