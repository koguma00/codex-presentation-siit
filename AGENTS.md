# Codex SIIT Presentation Guidance

## Research purpose

- Maintain a reusable Codex plugin for research-presentation authoring in the user's SIIT/KAIST visual style.
- Support a Google Slides-first narrative workflow, detailed PowerPoint finishing, and an inspectable HTML visual reference.
- Keep all published examples generic and free of private research content.

## Environment

- Use Python 3 standard library for packaging tests.
- Validate with `python3 -m unittest discover -s tests -v`.
- Validate the skill and plugin with the bundled Codex skill/plugin validators before release.

## Repository structure

- `plugins/siit-presentation/skills/siit-presentation/` is the canonical skill source.
- `references/` contains the workflow, layout catalogue, tokens, provenance, and visual rules.
- `assets/` contains sanitized PPTX/THMX seeds, SVG and HTML references, and institutional marks.
- `.agents/plugins/marketplace.json` is the installable marketplace entry.
- Never add the user's raw source deck, speaker notes, or non-public research material.
