# デジタル庁 イラストレーション・アイコン素材 Skill

このリポジトリは、**日本のデジタル庁が公開した「イラストレーション・アイコン素材」を、WebサイトやアプリのUIで適切に活用するためのエージェントskill**です。

公式素材ページ: [イラストレーション・アイコン素材｜デジタル庁](https://www.digital.go.jp/policies/servicedesign/designsystem/Illustration_Icons)

[日本語](#日本語) | [English](#english)

## 日本語

### インストール

```bash
npx skills add TakuroFukamizu/japan-digital-agency-illustration-icons-skill \
  --skill digital-agency-illustration-icons
```

Codexのみに追加する場合:

```bash
npx skills add TakuroFukamizu/japan-digital-agency-illustration-icons-skill \
  --skill digital-agency-illustration-icons \
  --agent codex
```

### このskillでできること

- UIの目的や文脈に合う素材を、日本語または英語の意味から検索する
- 必要なSVG・PNGだけをプロジェクトへコピーする
- アイコンのline/fill、PNGの24/48/72pxを選択する
- HTML、React、Next.jsへアクセシブルに実装する
- アスペクト比、コントラスト、代替テキスト、表示ラベルを確認する
- 素材を改変する場合の出典表示と変更内容の明示を確認する

### 収録内容

- SVGアイコン: 120点
- PNGアイコン: 360点
- PNGイラストレーション: 74点
- デジタル庁の公式ガイドラインPDF: 2点
- 公式利用規約
- 日本語・英語対応の素材検索／コピースクリプト

Skill本体は [`skills/digital-agency-illustration-icons/`](skills/digital-agency-illustration-icons/) にあります。

### 素材の権利と利用条件

収録している公式素材の著作権は、特記がない限りデジタル庁に帰属します。素材には本リポジトリのMITライセンスではなく、デジタル庁の[イラストレーション・アイコン素材利用規約](https://www.digital.go.jp/policies/servicedesign/designsystem/Illustration_Icons/terms_of_use)が適用されます。収録した規約は [`assets/official/LICENSE.txt`](skills/digital-agency-illustration-icons/assets/official/LICENSE.txt) からも確認できます。

公式利用規約では、商用利用を含む利用が認められており、未改変での利用には原則としてクレジット表記が不要です。編集・加工した素材を公表、利用または再配布する場合は、出典と変更内容を明示し、国や府省が編集後の素材を作成したように見せてはいけません。利用前に必ず最新の公式利用規約を確認してください。

---

## English

This repository provides an agent skill for using the official [Illustration and Icon Materials published by the Digital Agency, Government of Japan](https://www.digital.go.jp/en/policies/servicedesign/designsystem/Illustration_Icons) in web and app interfaces.

### Install

```bash
npx skills add TakuroFukamizu/japan-digital-agency-illustration-icons-skill \
  --skill digital-agency-illustration-icons
```

Install specifically for Codex:

```bash
npx skills add TakuroFukamizu/japan-digital-agency-illustration-icons-skill \
  --skill digital-agency-illustration-icons \
  --agent codex
```

### What this skill provides

- Semantic asset search in Japanese and English
- Deterministic copying of only the required SVG or PNG files
- Selection of line/fill icon styles and 24/48/72px PNG sizes
- Accessible implementation guidance for HTML, React, and Next.js
- Checks for proportions, contrast, alt text, and visible labels
- Attribution and change-disclosure guidance for modified assets

The bundled package contains 120 SVG icons, 360 PNG icon variants, 74 PNG illustrations, two official guideline PDFs, and the official terms.

### Asset rights

Unless otherwise noted, the official assets remain copyrighted by the Digital Agency. They are governed by the Digital Agency's [Illustration and Icon Materials Terms of Use](https://www.digital.go.jp/policies/servicedesign/designsystem/Illustration_Icons/terms_of_use), not by this repository's MIT license. The bundled copy is available at [`assets/official/LICENSE.txt`](skills/digital-agency-illustration-icons/assets/official/LICENSE.txt).

The official terms permit commercial use and generally do not require credit for unmodified assets. Published, used, or redistributed adaptations must identify the source and changes, and must not imply that the adapted material was created by the Government of Japan or one of its ministries. Check the current official terms before use.
