---
name: digital-agency-illustration-icons
description: Select, copy, and implement the Digital Agency, Government of Japan's official illustration and icon assets in accessible web and app interfaces. Use when designing or editing UI that needs Japanese administrative, identity, My Number, application, tax, family, health, navigation, status, or general public-service visuals; when replacing improvised icons with the Digital Agency asset set; or when reviewing use of these assets for accessibility, aspect ratio, format, and attribution requirements.
---

# Use Digital Agency Illustration and Icon Assets

Use the bundled, unmodified June 2023 official asset package. Choose assets by meaning, copy only the required files into the target project, and implement them as supporting—not sole—communication.

## Workflow

1. Inspect the target UI, framework, asset conventions, background colors, and existing accessibility patterns.
2. Decide between:
   - **Icon**: compact navigation, status, action, or administrative concept. Prefer SVG on the web.
   - **Large illustration**: overall service concept or landing/intro content.
   - **Medium illustration**: a specific procedure or scene.
   - **Small illustration**: a concrete object, card, device, hand, or person combined with text.
3. Search semantically instead of guessing filenames:

   ```bash
   python3 <skill-dir>/scripts/asset_tool.py search "tax payment"
   python3 <skill-dir>/scripts/asset_tool.py search "マイナンバーカード スマートフォン" --type illustration
   python3 <skill-dir>/scripts/asset_tool.py search "家族 健康 税金 通知 検索" --type icon
   python3 <skill-dir>/scripts/asset_tool.py search "tax payment" --type icon --match all
   python3 <skill-dir>/scripts/asset_tool.py list --type icon
   ```

   Searches match any query term by default so one request can discover assets for several independent UI concepts. Add `--match all` when every term must describe the same asset.

4. Inspect promising files visually before selecting one. For the complete meaning map, read `references/catalog.md`. For official visual rules, consult the bundled PDFs in `assets/official/icon/` or `assets/official/illustration/` when the choice or treatment is unclear.
5. Copy a selected asset with the tool:

   ```bash
   python3 <skill-dir>/scripts/asset_tool.py copy icon/tax --style line --format svg --dest <project-asset-dir>
   python3 <skill-dir>/scripts/asset_tool.py copy illustration/m_10_white --dest <project-asset-dir>
   ```

   Use `--format png --size 24|48|72` only when raster icon output is required. Do not copy the whole collection into an application unless explicitly requested.
6. Implement using the framework's normal asset mechanism. Preserve intrinsic proportions and do not stretch, crop, trace, redraw, recolor, or otherwise modify the artwork unless the user explicitly requests modification.
7. Apply the accessibility and licensing checks below, then run the project's relevant tests or build.

## Accessibility Requirements

- Keep the associated meaning in visible text. Never rely on an illustration or icon alone for an administrative procedure or service.
- Pair icons with visible labels. Treat a labeled icon as decorative: use `alt=""` for `<img>`, or `aria-hidden="true"` for inline SVG. Do not duplicate the visible label in an accessible name.
- Give a meaningful illustration concise alt text when it conveys information not already present nearby. Use `alt=""` when it is purely decorative or redundant.
- If space genuinely requires an icon-only control, give the control an accessible name and a target size of at least 44 × 44 CSS px.
- Include an icon and its label in the same link or button; never create adjacent duplicate interactive targets.
- Ensure icon color contrast against its background is at least 4.5:1. A 3:1 threshold is acceptable only when the icon is guaranteed to be exclusively non-text content.
- Do not put essential prose into an image. If the image contains complex information, provide that information in surrounding HTML or native UI text.

Read `references/implementation.md` before implementing inline SVG, React/Next.js components, CSS masks, or icon-only controls.

## Visual Rules

- Preserve a 1:1 icon aspect ratio. Prefer official SVG over rasterized or manually reconstructed versions.
- Use the provided line/fill variant consistently within the same navigation or control set; do not mix styles arbitrarily.
- Display icons at an intentional standard size. Official PNG sizes are 24, 48, and 72 px.
- Preserve illustration aspect ratio and whitespace. Do not crop a person, hand, device, or identifying document merely to fill a container; use `object-fit: contain`.
- Select `*_white` illustrations for white/transparent placement and `*_warmgray` variants when the supplied warm-gray panel is desired.
- Use the assets as supplementary UI imagery, not as evidence of government endorsement or authorship of the surrounding product.

## Usage Terms

The bundled assets are copyrighted by the Digital Agency and governed by `assets/official/LICENSE.txt`, not by the repository's software license.

- Unmodified use, redistribution, and commercial use are permitted without credit under the official terms.
- If editing or adapting an asset for publication, clearly state the source and what was changed, and never present the result as if the national government or a ministry created it.
- Before publishing a modified asset, read `references/terms-and-sources.md` and the bundled official terms in full.
- Treat the official website as authoritative if local material and the current site differ.

## Completion Checklist

- Confirm semantic fit; do not choose solely for visual similarity.
- Confirm visible text carries the meaning.
- Confirm alt text or accessible naming is correct and non-duplicative.
- Confirm aspect ratio, style consistency, and contrast.
- Confirm only required assets were copied and no accidental modification occurred.
- If modified, include the required source and change disclosure.
