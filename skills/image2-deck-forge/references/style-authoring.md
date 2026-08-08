# Style Authoring Contract

Create a style from visual references, a deck, a webpage, a document, or a precise written description.

## Separate signal from accident

Identify features repeated across references:

- color relationships and approximate ratios;
- typography mood and hierarchy;
- grid, margins, rhythm, and recurring page structures;
- container, divider, border, radius, shadow, and glow systems;
- photographic or illustrative treatment;
- repeated ornaments and their frequency;
- cover versus inner-page behavior;
- header, footer, metadata, logo, and date behavior;
- text-density ceiling;
- strongest negative constraints.

Treat one-off subjects, words, people, products, and page-specific compositions as content unless repetition proves they are style invariants.

## Ask only material questions

Ask about intended use, default ratio, text density, output package, fixed brand assets, language, and whether to save. Do not ask questions already answered by the references or request.

## Name the style

- Use a memorable human-facing name.
- Use a stable kebab-case filename.
- Add a small alias set based on appearance and use case.
- Avoid names that depend on a private client, confidential project, or trademark unless the user has the right to publish it.

## Required file structure

Every style file must include:

- `# Style Name`
- `## Identity`
- `## Use`
- `## Visual DNA`
- `## Style Lock`
- `## Page Behavior`
- `## Prompt Prefix`
- `## Quality Gate`

The Style Lock must define:

- typography mood and title/body hierarchy;
- language behavior;
- relative type scale;
- grid, safe margins, and rhythm;
- stable component, border, container, divider, and arrow system;
- palette with at least four hex values and approximate ratios;
- cover versus inner-slide behavior;
- image or illustration treatment;
- header, footer, date, logo, and watermark behavior;
- text-density limit;
- style-isolation rules;
- explicit Image 2 negative constraints.

## Semantic image rule

For styles that allow varied imagery, require every page prompt to state:

1. the page's core claim;
2. the selected visual anchor;
3. why the anchor explains, proves, contrasts, or strengthens the claim.

Reject an image choice justified only by ?it looks technological,? ?it feels premium,? or another subject-free mood statement.

## Register the style

Add the filename, aliases, best use, signature, and avoid conditions to `styles/catalog.md`. Keep catalog entries mutually distinguishable.

Run:

```bash
python scripts/validate_style_library.py
```

Fix every error before using or publishing the new style.
