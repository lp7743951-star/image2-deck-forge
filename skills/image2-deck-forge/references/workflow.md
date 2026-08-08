# Creation Workflow

## 1. Read the source

Extract:

- audience and presentation setting;
- one-sentence thesis;
- 3-6 supporting claims;
- evidence that must remain accurate;
- desired audience action;
- concepts that can become visual anchors;
- source language, tone, and terminology that must be preserved.

Do not copy long paragraphs into slides. Rewrite source language into presentation language.

## 2. Resolve production parameters

Use these defaults unless the request says otherwise:

- ratio: 16:9;
- language: Chinese-first;
- density: low;
- output: individual slide images, plus image-only PPTX when the user asks for a PPT;
- quality: high-resolution Image 2 output;
- dates and brand marks: absent;
- style: best content fit from `styles/catalog.md`.

Ask only for missing information that materially changes output. Ask for slide count when the user has neither specified it nor delegated the decision. If delegated, recommend a count from source length and story complexity.

## 3. Select one style

1. Match explicit style names and aliases first.
2. Otherwise compare content against the catalog's best-use and avoid columns.
3. Prefer the narrowest clear fit:
   - developer tools and system workflows -> terminal tech;
   - cross-domain institutional strategy -> impact grid;
   - climate and ESG evidence -> climate impact;
   - fashion, lifestyle, and consumer commerce -> French editorial;
   - broad future, AI, product, culture, or innovation narratives needing semantic imagery -> aubergine future.
4. Ask one short question when two styles remain equally plausible.
5. Read the complete chosen style file.
6. Copy its Style Lock into `prompts.md` without weakening it.

## 4. Build the story arc

Assign every page a role and one claim. Use `page-types.md`.

A compact deck normally uses:

1. cover;
2. context or tension;
3. central claim;
4. evidence, comparison, framework, or process;
5. implications;
6. action or conclusion.

Longer decks may add contents and section dividers. Do not add a contents slide merely to make a short deck look formal.

## 5. Write outline.md

Use this schema for every page:

```markdown
## Slide 01 - Cover
- Role:
- Core claim:
- Visible title:
- Takeaway or subtitle:
- Information points:
- Visual anchor:
- Why this anchor supports the claim:
- Source evidence:
```

Keep visible copy short. A normal inner slide gets at most 2-3 short information points.

## 6. Write prompts.md

Start with:

- production parameters;
- full selected Style Lock;
- global language, density, logo, date, and outer-border rules;
- thumbnail-board prompt when applicable.

Then write one page block:

```markdown
## Slide 01
- Page role: cover
- Core claim:
- Exact visible text:
- Composition:
- Semantic visual anchor:
- Relevance:
- Style Lock: apply the complete shared lock above
- Negative constraints:
```

Every inner-slide prompt must explicitly require information-first composition, quiet background, restrained ornament, and readable hierarchy.

## 7. Stop for approval

Show or link `outline.md` and `prompts.md`. Do not generate images until the user approves them unless the user explicitly waives this gate.

## 8. Lock rhythm with a thumbnail board

Use a thumbnail board when a deck has multiple pages or visual consistency is important.

- Prefer 4, 6, 9, or 16 slots.
- Use the smallest stable grid that contains the planned slides.
- Turn spare slots into style-system reference tiles.
- Compose every tile in the final slide aspect ratio.
- Use only enough text to identify the page.
- Judge rhythm, palette, whitespace, image placement, grid, and page variation.
- Treat the board as planning evidence, never as final slides.

## 9. Generate final slides

Generate one slide per Image 2 output. Use the approved board as continuity reference, plus the full Style Lock and page-specific prompt.

Name files in order:

```text
slide-01.png
slide-02.png
slide-03.png
```

Do not accept a combined sheet as the final deck. Regenerate pages with unreadable text, wrong ratios, style contamination, border drift, irrelevant imagery, or outer-canvas frames.

## 10. Review, revise, and package

Present all page images for review. Preserve approved pages. Follow `revision.md` for changes. After every image is approved, follow `output-contract.md` to assemble and package the final deliverables.
