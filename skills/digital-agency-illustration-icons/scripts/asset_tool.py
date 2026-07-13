#!/usr/bin/env python3
"""Search and copy bundled Digital Agency illustration and icon assets."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
import unicodedata
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parent.parent
ASSET_ROOT = SKILL_ROOT / "assets" / "official"

ICON_KEYWORDS = {
    "add": "追加 plus create 新規",
    "application": "申請 application request 手続き",
    "arrival": "到着 arrival entry 入国",
    "arrow_down": "下 矢印 arrow down expand",
    "arrow_left": "左 矢印 arrow left back previous 戻る",
    "arrow_right": "右 矢印 arrow right next forward 次",
    "arrow_up": "上 矢印 arrow up collapse",
    "attention": "注意 警告 warning alert caution",
    "authentication": "認証 authentication verify login 本人確認",
    "bank_account": "銀行口座 bank account 金融機関",
    "certification": "証明 certification certificate 証明書",
    "certification_with_seal": "証明 印鑑 seal certificate 証明書",
    "child": "こども 子供 child kids",
    "code_reader": "コードリーダー QR barcode scanner 読み取り",
    "complete": "完了 complete success check done",
    "copy": "コピー copy duplicate 複製",
    "departure": "出発 departure exit 出国",
    "documents": "書類 documents files paperwork",
    "download": "ダウンロード download save 保存",
    "e_application": "電子申請 online e-application digital 手続き",
    "expenditure": "支出 expenditure expense spending 支払い",
    "family": "家族 family household 世帯",
    "fast_track": "ファストトラック fast track shortcut 迅速",
    "fillable_card": "記入可能カード fillable card form 入力",
    "health": "健康 health healthcare 医療",
    "help": "ヘルプ help question support 問い合わせ",
    "history": "履歴 history recent log 過去",
    "house": "住まい 家 house home residence 住宅",
    "immunization": "予防接種 vaccination immunization vaccine ワクチン",
    "inbox": "受信 inbox tray box 受付",
    "income": "収入 income earnings 給与",
    "information": "情報 information info 案内",
    "invoice": "請求書 invoice bill payment",
    "itinerary": "旅程 itinerary route schedule 経路",
    "laws": "法令 laws legal regulation 規則",
    "luggage": "荷物 luggage baggage 手荷物",
    "mailing": "郵送 mailing post mail 郵便",
    "me": "本人 自分 me person account user",
    "medicine": "薬 medicine medication pharmacy 医薬品",
    "menu": "メニュー menu navigation hamburger",
    "money": "お金 money cash payment 支払い",
    "mother_and_child": "母子 mother child parent baby 親子",
    "municipality": "自治体 municipality city hall 行政 市役所",
    "new_window": "別ウィンドウ new window external link 外部リンク",
    "notification": "通知 notification bell お知らせ",
    "password": "パスワード password key security セキュリティ",
    "pension": "年金 pension retirement 老後",
    "personal_computer": "パソコン computer PC desktop laptop",
    "printer": "印刷 printer print プリンター",
    "privacy_protection": "プライバシー 保護 privacy protection security shield",
    "public_offering": "公募 public offering recruitment 募集",
    "search": "検索 search find magnifier 探す",
    "seal_certificate": "印鑑証明 seal certificate stamp 証明",
    "smartphone": "スマートフォン smartphone mobile phone 携帯",
    "specialist": "専門家 specialist expert professional",
    "stamp": "印鑑 stamp seal はんこ",
    "tax": "税 tax taxation 税金 納税",
    "transactions": "取引 transactions exchange transfer 手続き",
    "update": "更新 update refresh reload",
    "work": "仕事 work job employment 職業",
}

ILLUSTRATION_KEYWORDS = {
    "l_01_rectangle_white": "digital public service people family support パソコン 人々 家族 デジタルサービス 横長",
    "l_01_square_white": "digital public service people family support パソコン 人々 家族 デジタルサービス 正方形",
    "l_02_rectangle_white": "smartphone card overhead hands スマートフォン カード 手俯瞰 横長",
    "l_02_square_white": "smartphone card overhead hands スマートフォン カード 手俯瞰 正方形",
    "m_01_warmgray": "card smartphone complete check カード スマートフォン 完了 確認 グレー背景",
    "m_01_white": "card smartphone complete check カード スマートフォン 完了 確認 白背景",
    "m_02_warmgray": "hand smartphone complete check 手 スマートフォン 完了 確認 グレー背景",
    "m_02_white": "hand smartphone complete check 手 スマートフォン 完了 確認 白背景",
    "m_03_warmgray": "smartphone warning error alert スマートフォン 警告 エラー 注意 グレー背景",
    "m_03_white": "smartphone warning error alert スマートフォン 警告 エラー 注意 白背景",
    "m_04_warmgray": "smartphone maintenance settings repair スマートフォン メンテナンス 設定 修理 グレー背景",
    "m_04_white": "smartphone maintenance settings repair スマートフォン メンテナンス 設定 修理 白背景",
    "m_05_warmgray": "smartphone QR code display スマートフォン QRコード 表示 グレー背景",
    "m_05_white": "smartphone QR code display スマートフォン QRコード 表示 白背景",
    "m_06_warmgray": "scan read QR code smartphone 読み取り スキャン QRコード グレー背景",
    "m_06_white": "scan read QR code smartphone 読み取り スキャン QRコード 白背景",
    "m_07_warmgray": "smartphone identity My Number card マイナンバーカード スマートフォン 本人確認 グレー背景",
    "m_07_white": "smartphone identity My Number card マイナンバーカード スマートフォン 本人確認 白背景",
    "m_08_warmgray": "smartphone reader kiosk terminal スマートフォン 読取機 端末 グレー背景",
    "m_08_white": "smartphone reader kiosk terminal スマートフォン 読取機 端末 白背景",
    "m_09_warmgray": "hand holding identity My Number card 手 マイナンバーカード 本人確認 グレー背景",
    "m_09_white": "hand holding identity My Number card 手 マイナンバーカード 本人確認 白背景",
    "m_10_warmgray": "person laptop computer online 人 パソコン オンライン グレー背景",
    "m_10_white": "person laptop computer online 人 パソコン オンライン 白背景",
    "m_11_warmgray": "person service counter consultation support 窓口 相談 支援 グレー背景",
    "m_11_white": "person service counter consultation support 窓口 相談 支援 白背景",
    "m_12_warmgray": "people hand card identity counter カード 手渡す 対面 本人確認 グレー背景",
    "m_12_white": "people hand card identity counter カード 手渡す 対面 本人確認 白背景",
    "m_13_warmgray": "face portrait identity verification 顔 写真 本人確認 照合 グレー背景",
    "m_13_white": "face portrait identity verification 顔 写真 本人確認 照合 白背景",
    "m_14_warmgray": "smartphone payment card terminal 決済 支払い カード端末 グレー背景",
    "m_14_white": "smartphone payment card terminal 決済 支払い カード端末 白背景",
    "s_01": "My Number identity card front マイナンバーカード 表面 個人番号カード",
    "s_02": "identity card back IC chip QR code カード 裏面 ICチップ QRコード",
    "s_03": "health insurance card 健康保険証 保険証",
    "s_04": "passport cover パスポート 旅券 表紙",
    "s_05": "open passport pages パスポート 旅券 開く",
    "s_06": "passport identity page パスポート 旅券 顔写真",
    "s_07": "identity card front ID card カード 表面",
    "s_08": "card back ID card カード 裏面",
    "s_09": "passport cover パスポート 旅券 表紙",
    "s_10": "document form paper 書類 申請書 用紙",
    "s_11": "card holder case identity カード ケース ホルダー",
    "s_12": "smartphone device dark スマートフォン 端末",
    "s_13": "smartphone device light screen スマートフォン 端末 画面",
    "s_14": "smartphone screen detail display スマートフォン 画面 詳細",
    "s_hand01": "hand smartphone landscape horizontal 手 スマートフォン 横向き",
    "s_hand02": "hand smartphone portrait vertical light skin 手 スマートフォン 縦向き",
    "s_hand03": "hand smartphone portrait vertical dark skin 手 スマートフォン 縦向き",
    "s_hand04": "point tap finger hand 指 タップ 手",
}

for number in range(1, 19):
    ILLUSTRATION_KEYWORDS[f"s_human{number:02d}"] = (
        "diverse person portrait face human head shoulders "
        "多様な人物 人 顔 上半身 ポートレート"
    )
for number in range(19, 25):
    ILLUSTRATION_KEYWORDS[f"s_human{number:02d}"] = (
        "diverse person full body standing human "
        "多様な人物 人 全身 立つ"
    )


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).lower()
    return " ".join(value.replace("_", " ").replace("-", " ").split())


def entries(asset_type: str | None = None) -> list[dict[str, str]]:
    result: list[dict[str, str]] = []
    if asset_type in (None, "icon"):
        for name, keywords in sorted(ICON_KEYWORDS.items()):
            result.append(
                {
                    "id": f"icon/{name}",
                    "type": "icon",
                    "description": keywords,
                }
            )
    if asset_type in (None, "illustration"):
        for name, keywords in sorted(ILLUSTRATION_KEYWORDS.items()):
            result.append(
                {
                    "id": f"illustration/{name}",
                    "type": "illustration",
                    "description": keywords,
                }
            )
    return result


def score_entry(entry: dict[str, str], query: str) -> int:
    query_norm = normalize(query)
    identifier = normalize(entry["id"])
    haystack = normalize(f'{entry["id"]} {entry["description"]}')
    if not query_norm:
        return 1
    score = 0
    if query_norm == identifier or query_norm == identifier.split(" ", 1)[-1]:
        score += 100
    if query_norm in haystack:
        score += 40
    for token in query_norm.split():
        if token in identifier:
            score += 15
        elif token in haystack:
            score += 6
        else:
            score -= 3
    return score


def emit(items: list[dict[str, str]], as_json: bool) -> None:
    if as_json:
        print(json.dumps(items, ensure_ascii=False, indent=2))
        return
    if not items:
        print("No matching assets.")
        return
    width = max(len(item["id"]) for item in items)
    for item in items:
        print(f'{item["id"]:<{width}}  {item["description"]}')


def command_search(args: argparse.Namespace) -> int:
    ranked = []
    for entry in entries(args.type):
        score = score_entry(entry, args.query)
        if score > 0:
            ranked.append((score, entry))
    ranked.sort(key=lambda pair: (-pair[0], pair[1]["id"]))
    emit([entry for _, entry in ranked[: args.limit]], args.json)
    return 0 if ranked else 1


def command_list(args: argparse.Namespace) -> int:
    emit(entries(args.type), args.json)
    return 0


def resolve_source(args: argparse.Namespace) -> Path:
    try:
        asset_type, name = args.asset_id.split("/", 1)
    except ValueError as error:
        raise ValueError("Asset ID must look like icon/tax or illustration/m_10_white") from error

    if asset_type == "icon":
        if name not in ICON_KEYWORDS:
            raise ValueError(f"Unknown icon: {name}")
        if args.format == "svg":
            filename = f"{name}_{args.style}.svg"
            return ASSET_ROOT / "icon" / "svg" / filename
        filename = f"{name}_{args.style}{args.size}.png"
        return ASSET_ROOT / "icon" / "png" / filename
    if asset_type == "illustration":
        if name not in ILLUSTRATION_KEYWORDS:
            raise ValueError(f"Unknown illustration: {name}")
        if args.format != "png":
            raise ValueError("Official illustrations are available only as PNG")
        return ASSET_ROOT / "illustration" / "png" / f"{name}.png"
    raise ValueError("Asset type must be icon or illustration")


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(block)
    return hasher.hexdigest()


def command_copy(args: argparse.Namespace) -> int:
    try:
        source = resolve_source(args)
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    if not source.is_file():
        print(f"error: bundled source is missing: {source}", file=sys.stderr)
        return 2

    destination_dir = Path(args.dest).expanduser().resolve()
    destination = destination_dir / source.name
    if destination.exists() and not args.force:
        if destination.is_file() and digest(destination) == digest(source):
            print(f"Already identical: {destination}")
            return 0
        print(f"error: destination exists; use --force to replace: {destination}", file=sys.stderr)
        return 2

    if args.dry_run:
        print(f"Would copy {source} -> {destination}")
        return 0
    destination_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    print(f"Copied: {destination}")
    print("Asset remains subject to assets/official/LICENSE.txt in this skill.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Search and copy bundled Digital Agency UI assets."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    search = subparsers.add_parser("search", help="Search by Japanese or English meaning")
    search.add_argument("query")
    search.add_argument("--type", choices=("icon", "illustration"))
    search.add_argument("--limit", type=int, default=12)
    search.add_argument("--json", action="store_true")
    search.set_defaults(handler=command_search)

    list_parser = subparsers.add_parser("list", help="List known assets")
    list_parser.add_argument("--type", choices=("icon", "illustration"))
    list_parser.add_argument("--json", action="store_true")
    list_parser.set_defaults(handler=command_list)

    copy = subparsers.add_parser("copy", help="Copy one official asset into a project")
    copy.add_argument("asset_id")
    copy.add_argument("--style", choices=("line", "fill"), default="line")
    copy.add_argument("--format", choices=("svg", "png"), default=None)
    copy.add_argument("--size", choices=(24, 48, 72), type=int, default=24)
    copy.add_argument("--dest", required=True)
    copy.add_argument("--force", action="store_true")
    copy.add_argument("--dry-run", action="store_true")
    copy.set_defaults(handler=command_copy)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "copy" and args.format is None:
        args.format = "svg" if args.asset_id.startswith("icon/") else "png"
    return args.handler(args)


if __name__ == "__main__":
    raise SystemExit(main())
