# Output Contract

## Final image rules

- Deliver one independently usable image per slide.
- Preserve one aspect ratio and pixel geometry across the set.
- Use ordered two-digit names such as `slide-01.png`.
- Never treat a thumbnail board, storyboard, contact sheet, PDF page collage, or multi-slide image as a final slide.
- Keep approved images immutable while revising rejected pages.

## Image-only PPTX

Create a PPTX only when the user asks for a presentation file or package.

- Match slide dimensions to the image aspect ratio.
- Place one page image full bleed on each slide.
- Preserve exact page order.
- Do not recreate text, charts, or shapes as editable objects.
- Do not crop, stretch, add margins, add borders, or change color during assembly.
- Verify the first, middle, and last slides after assembly.

If the user needs fully editable text, charts, and shapes, explain that this Skill produces image-only PPTX and route the work to a normal presentation-authoring workflow.

## Approval gate

Do not create the final PPTX or zip until the user approves all slide images. A request to revise one page reopens the approval gate for that page and the assembled package.

## Package layout

Use a dedicated project directory:

```text
project-slug/
|-- deck.pptx
|-- images/
|   |-- slide-01.png
|   |-- slide-02.png
|   +-- ...
|-- outline.md
|-- prompts.md
|-- style-used.md
|-- thumbnail-board.png
|-- revision-log.md
+-- project-slug.zip
```

Include the thumbnail board only when used. Include `revision-log.md` only after revisions.

## style-used.md

Record:

- selected style name and file;
- why it fits;
- full Style Lock;
- any user-approved deviations;
- ratio, language, density, and output type.

## Final verification

Before delivery, confirm:

- image count equals slide count;
- file numbering has no gaps or duplicates;
- every image has the requested ratio;
- all images use the selected Style Lock;
- the PPTX page count and order match the image set;
- no page has an outer black frame, unreadable text, unverified date, or drifting generated logo;
- the zip contains every required artifact and no unrelated source file.
