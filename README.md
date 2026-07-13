# Digital Agency Illustration & Icons Skill

An agent skill for selecting and implementing the Digital Agency, Government of Japan's official illustration and icon assets in accessible web and app interfaces.

## Install

After publishing this repository to GitHub:

```bash
npx skills add <owner>/digital-agency-illustration-icons-skill --skill digital-agency-illustration-icons
```

Install specifically for Codex:

```bash
npx skills add <owner>/digital-agency-illustration-icons-skill --skill digital-agency-illustration-icons --agent codex
```

Test the local repository before publishing:

```bash
npx skills add . --list
```

The installable skill lives at `skills/digital-agency-illustration-icons/`.

## What it provides

- The official June 2023 package: 120 SVG icons, 360 PNG icon variants, 74 PNG illustrations, two guideline PDFs, and the official terms.
- Semantic Japanese/English asset search and deterministic copying.
- Accessible HTML, React, and Next.js implementation guidance.
- Guardrails for proportions, line/fill consistency, contrast, alt text, and edited-asset attribution.

## Asset rights

The official assets remain copyrighted by the Digital Agency and are governed by [`assets/official/LICENSE.txt`](skills/digital-agency-illustration-icons/assets/official/LICENSE.txt). They are not covered by this repository's MIT license. The official terms allow commercial use and unmodified use without credit; edited or adapted assets require source and change disclosure and must not be presented as government-created.

Official source: https://www.digital.go.jp/policies/servicedesign/designsystem/Illustration_Icons
