# TIL: Typst

Typst is popping up more and more, so it’s worth understanding where it fits.

## What is Typst?

**Typst** is a **modern typesetting system** (like LaTeX), but designed with:

* a **simple, readable syntax** (closer to Markdown)
* **fast compilation**
* **built-in scripting** (without TeX’s arcane macro language)
* **great defaults** for documents, papers, slides, etc.

Think of it as:

> *“LaTeX power, Markdown simplicity, modern tooling.”*

---

## Typst vs Markdown

| Feature                  | Markdown                    | Typst                                  |
| ------------------------ | --------------------------- | -------------------------------------- |
| Purpose                  | Lightweight text formatting | Full typesetting system                |
| Learning curve           | Very low                    | Low–medium                             |
| Math                     | Limited / extensions        | First-class, built-in                  |
| Layout control           | Minimal                     | Strong (margins, grids, columns, etc.) |
| Logic (loops, functions) | No                          | Yes                                    |
| Output quality           | Basic                       | Publication-grade                      |
| Typical use              | README, docs, notes         | Papers, reports, books, slides         |


👉 **Markdown is for writing text**

👉 **Typst is for designing documents**

---

## Typst vs LaTeX

| Feature        | LaTeX               | Typst                       |
| -------------- | ------------------- | --------------------------- |
| Syntax         | Verbose, cryptic    | Clean, readable             |
| Error messages | Painful 😅          | Actually helpful            |
| Compile speed  | Slow                | Very fast                   |
| Macros         | Powerful but scary  | Built-in scripting language |
| Tooling        | 40 years of baggage | Modern, consistent          |
| Learning curve | Steep               | Gentle                      |
| Ecosystem      | Huge                | Growing fast                |

Example:

**LaTeX**

```tex
\section{Introduction}
\textbf{Hello} world!
```

**Typst**

```typst
= Introduction
*Hello* world!
```

Same result, much nicer.

---

## Where does Typst render?

You have several options:

### 1. **Typst Web App (official)**

* [https://typst.app](https://typst.app)
* Live preview in the browser
* Exports **PDF**
* Like Overleaf, but fast

### 2. **Local CLI**

```bash
typst compile doc.typ
```

Outputs PDF (or PNG/SVG).

### 3. **VS Code Extension**

* Live preview
* Very smooth workflow

---

## Do GitHub / GitLab support Typst?

### ✅ Partially

| Platform   | Native `.typ` Rendering | Notes / Workarounds                                                                                                                                                                     |
| ---------- | ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GitHub** | ❌ Renders as plain text | * Commit Typst files in repos<br>* No native preview like Markdown<br>* Commit compiled PDFs<br>* Use GitHub Actions to auto-build PDFs from Typst                                      |
| **GitLab** | ❌ Renders as plain text | * Commit Typst files in repos<br>* No native preview in the web UI<br>* Use GitLab CI/CD to compile Typst → PDF<br>* Optional: Typst.app can sync with GitLab (experimental / Pro plan) |

### Typical Workflow

```
doc.typ → CI pipeline → doc.pdf → artifact / commit
```

> Both GitHub and GitLab treat Typst as a **source file**; you need to compile it separately to view the rendered document.

---

## Does Jupyter support Typst?

### ❌ Not natively (yet)

But you have workarounds:

### 1. Export Typst → PDF, then display

```python
from IPython.display import IFrame
IFrame("doc.pdf", width=800, height=600)
```

### 2. Use Typst for final documents

* Write analysis in notebook
* Export results (tables/figures)
* Include them in Typst

This is actually a **very common workflow** for research now.

---

## When should you use Typst?

Use **Typst** if you want:

* clean PDFs
* less pain than LaTeX
* more power than Markdown
* reproducible documents
* fast iteration

Use **Markdown** for:

* READMEs
* quick docs
* GitHub content
* notes

Use **LaTeX** if:

* you’re stuck with a journal template 😄
* you need some exotic package
* legacy reasons
