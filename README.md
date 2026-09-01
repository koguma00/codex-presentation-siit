# Codex SIIT Presentation

A Codex plugin for creating research presentations in the user's preferred SIIT/KAIST visual system.

## Workflow

1. Develop and revise the story in Google Slides.
2. Keep all editable text in `Noto Sans KR`.
3. Move to PowerPoint after the narrative and visible copy are stable.
4. Finish master application, exact alignment, spacing, line breaks, figure treatment, and export checks in PowerPoint.
5. Use the bundled HTML, SVG, PPTX, and THMX references to keep the design consistent across devices.

If Google Slides cannot be accessed or edited during the drafting stage, ask the user how to
proceed. Do not automatically replace the agreed Slides workflow with PPTX or HTML.

The published reference deck is sanitized and contains generic content only. The user's raw example deck is not included.

## Install

```bash
codex plugin marketplace add https://github.com/koguma00/codex-presentation-siit.git --ref main
codex plugin add siit-presentation@siit-presentation
```

Start a new Codex conversation after installation. Invoke the skill with `$siit-presentation` or ask to use the saved SIIT presentation design.

## Validate

```bash
python3 -m unittest discover -s tests -v
```
