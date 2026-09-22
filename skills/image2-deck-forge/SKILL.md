---
name: image2-deck-forge
description: Create, restyle, revise, and package image-first presentations and style-driven posters with Image 2 and reusable visual Style Locks. Use when turning source material into slide images or an image-only PPTX, extracting or saving a presentation style, selecting saved styles, or revising generated pages. Includes terminal-tech, institutional editorial, climate-impact, French commerce, aubergine semantic-future, and Orbit Flow / 星环流光 visual systems.
---

# Image 2 Deck Forge

Create coherent visual decks by treating style as a reusable control system rather than a loose mood. Generate every visual page with Image 2, then package approved page images into an image-only PPTX when requested.

## Enforce the non-negotiables

- Use Image 2 for every slide image, thumbnail board, infographic, article visual, and visual planning artifact.
- Do not use HTML/CSS, browser screenshots, SVG mockups, canvas, PIL, or local rendering as a substitute or intermediate visual.
- Stop and state that Image 2 access is required when it is unavailable.
- Generate one final image per slide. Never use a contact sheet as the final slide deliverable.
- Apply exactly one saved style and one complete Style Lock per deck unless the user explicitly requests a hybrid.
- Generate `outline.md` and `prompts.md` before producing a multi-page deck. Wait for approval unless the user explicitly waives the checkpoint.
- Do not generate the final PPTX or zip until the user approves every slide image.
- Treat PPTX as a full-bleed image container, not an editable layout source.
- Default to Chinese-first visible text and support documents unless the user requests another language.
- Do not add dates, timestamps, logos, wordmarks, or watermarks by default. Verify required dates and add brand marks later as fixed assets.

## Load only the needed guidance

- Read [styles/catalog.md](styles/catalog.md) whenever selecting, listing, or comparing styles.
- Read the complete selected style file before writing prompts.
- Read [references/workflow.md](references/workflow.md) for creation and document-to-deck work.
- Read [references/page-types.md](references/page-types.md) when mapping the story to slide roles.
- Read [references/output-contract.md](references/output-contract.md) when assembling or packaging deliverables.
- Read [references/style-authoring.md](references/style-authoring.md) when extracting, creating, renaming, or updating a style.
- Read [references/revision.md](references/revision.md) for post-generation changes.

## Route the request

### Create a deck

1. Inspect the source and identify audience, purpose, one-sentence thesis, evidence, desired action, and visual moments.
2. Resolve page count, ratio, output type, language exception, and density only when they materially affect the result.
3. Select a style through the catalog. Prefer an explicit style name; otherwise choose by content fit. Ask one short question only when the top two styles are genuinely tied.
4. Build the outline, page roles, Style Lock, thumbnail-board prompt, and page prompts.
5. Pause for approval.
6. Generate the thumbnail board when cross-page consistency matters, then generate each final page separately.
7. Review page images with the user, revise only rejected pages, and package only after full approval.

### Extract or save a style

1. Inspect all supplied references.
2. Separate invariant visual DNA from one-off content.
3. Follow the contract in [references/style-authoring.md](references/style-authoring.md).
4. Create a stable kebab-case file under `styles/`, add it to the catalog, and run `python scripts/validate_style_library.py`.
5. Never overwrite a built-in style unless the user explicitly requests an update.

### Revise a deck

1. Identify the exact slide and requested change.
2. Preserve the selected style, aspect ratio, approved content, and untouched pages.
3. Rewrite only the target page prompt and regenerate only that image.
4. Replace the corresponding PPTX page image and rebuild the package after approval.

### List or compare styles

Read [styles/catalog.md](styles/catalog.md). Return style name, best use, signature, and avoid conditions. Do not load every full style file unless the user asks for a detailed comparison.

## Apply the generation gates

Before Image 2 generation, confirm that:

- every slide has one core claim and one page type;
- normal inner slides have one title, one short takeaway, and at most 2-3 short information points;
- `prompts.md` includes the selected style's complete Style Lock;
- every page prompt declares `cover`, `section`, or `inner slide`;
- inner-slide prompts demand information-first layout, quiet support imagery, restrained ornament, and readable hierarchy;
- thumbnail tiles use the same aspect ratio as final slides;
- the deck uses one border, container, divider, arrow, header, and footer system;
- visual anchors explain the page meaning rather than merely looking futuristic;
- the prompt forbids style contamination, unreadable text, outer-canvas borders, and model-generated brand marks.

## Use the built-in styles

- `terminal-tech-magazine`: dark technical editorial for AI, developer tools, systems, and product workflows.
- `impact-grid-editorial`: warm-white institutional consulting and cross-domain impact reporting.
- `climate-impact-editorial-grid`: climate, ESG, sustainability, and environmental research.
- `french-editorial-commerce`: fashion, lifestyle, consumer brands, and premium commerce.
- `aubergine-semantic-future`: deep-plum future editorial with semantic image selection for AI, strategy, product, culture, and innovation.
- `orbit-flow-keynote` / `Orbit Flow` / `星环流光` / `白底星环` / `紫橙流光`: white business-tech layouts with a cropped blue orbital vortex, violet-orange flow, bold Chinese titles, numbered modules, and a navy conclusion band. Use for workshops, AI applications, product keynotes, and portrait information posters.

For Orbit Flow, read [styles/orbit-flow-keynote.md](styles/orbit-flow-keynote.md). Reflow portrait references for 16:9 slides; keep brush titles confined to covers and keep source brands, dates, and QR codes out of public samples.

Do not treat `impact-grid-editorial` and `climate-impact-editorial-grid` as duplicates: use the first for broad institutional or consulting narratives and the second when climate or environmental evidence is part of the subject.

## Finish with a hard quality gate

Reject or regenerate slides that contain unreadable text, mixed visual systems, a black frame on the outer canvas, repeated irrelevant robots, decorative fake UI, unverified dates, drifting logos, dense paragraphs, inconsistent headers, or cover-level visual noise on normal inner pages.
