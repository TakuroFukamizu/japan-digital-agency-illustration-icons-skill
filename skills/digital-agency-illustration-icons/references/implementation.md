# Accessible implementation patterns

## Labeled icon

Keep the icon silent because the visible text supplies the name.

```html
<a href="/search" class="nav-item">
  <img src="/assets/digital-agency/search_line.svg" alt="" width="24" height="24">
  <span>検索</span>
</a>
```

For inline SVG, add `aria-hidden="true"` and `focusable="false"`. Keep the SVG inside the same link or button as its label.

## Icon-only button

Use only when the layout cannot accommodate a visible label. Name the button, not the decorative image.

```html
<button type="button" aria-label="検索" class="icon-button">
  <img src="/assets/digital-agency/search_line.svg" alt="" width="24" height="24">
</button>
```

```css
.icon-button {
  inline-size: 44px;
  block-size: 44px;
  display: inline-grid;
  place-items: center;
}
```

## Informative and decorative illustrations

Use concise alt text only for information that surrounding text does not already communicate.

```html
<img
  src="/assets/digital-agency/m_05_white.png"
  alt="スマートフォンに表示したQRコード"
  width="512"
  height="512"
>
```

If the nearby heading and prose already explain the same scene, use `alt=""`. Never use filenames such as `m_05_white` as alt text.

## React and Next.js

Import static assets or place them under the project's public asset directory according to existing conventions. Preserve explicit dimensions to avoid layout shift. With `next/image`, set meaningful `alt` or an empty string using the same rules as native `<img>`.

Do not paste official SVG markup into JSX merely to avoid an asset request. Referencing the original file reduces accidental modifications. Inline it only when the project already has a controlled SVG pipeline and inline behavior is needed.

## Sizing and layout

```css
.service-illustration {
  display: block;
  max-inline-size: 100%;
  block-size: auto;
  object-fit: contain;
}

.ui-icon {
  inline-size: 1.5rem;
  block-size: 1.5rem;
  flex: none;
}
```

Do not set both width and height to unrelated values. Do not use `object-fit: cover` when it crops the artwork. Verify contrast in the actual rendered state, including hover, disabled, selected, and dark-mode backgrounds.
