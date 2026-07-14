from __future__ import annotations

import importlib.util
import types
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
TOOL_PATH = (
    REPO_ROOT
    / "skills"
    / "digital-agency-illustration-icons"
    / "scripts"
    / "asset_tool.py"
)

spec = importlib.util.spec_from_file_location("asset_tool", TOOL_PATH)
assert spec and spec.loader
asset_tool = importlib.util.module_from_spec(spec)
spec.loader.exec_module(asset_tool)


class SearchTests(unittest.TestCase):
    def ids(self, query: str, **kwargs: object) -> list[str]:
        return [entry["id"] for entry in asset_tool.search_entries(query, **kwargs)]

    def test_multi_concept_query_returns_each_requested_icon(self) -> None:
        results = set(
            self.ids(
                "家族 健康 税金 通知 検索",
                asset_type="icon",
                limit=12,
            )
        )
        self.assertTrue(
            {
                "icon/family",
                "icon/health",
                "icon/tax",
                "icon/notification",
                "icon/search",
            }.issubset(results)
        )

    def test_ui_status_terms_resolve_to_semantic_icons(self) -> None:
        expectations = {
            "確認待ち": "icon/application",
            "処理中": "icon/update",
            "要確認": "icon/attention",
            "完了済み": "icon/complete",
        }
        for query, expected in expectations.items():
            with self.subTest(query=query):
                self.assertEqual(
                    self.ids(query, asset_type="icon", limit=1)[0],
                    expected,
                )

    def test_all_match_requires_every_term(self) -> None:
        results = self.ids(
            "税金 支払い",
            asset_type="icon",
            match_mode="all",
            limit=10,
        )
        self.assertEqual(results, ["icon/tax"])

    def test_punctuation_is_treated_as_a_separator(self) -> None:
        spaced = self.ids("家族 健康", asset_type="icon", limit=10)
        punctuated = self.ids("家族、健康", asset_type="icon", limit=10)
        self.assertEqual(spaced, punctuated)

    def test_unknown_query_returns_no_results(self) -> None:
        self.assertEqual(
            self.ids("存在しない検索語xyz", asset_type="icon"),
            [],
        )


class CatalogTests(unittest.TestCase):
    def test_catalog_matches_bundled_assets(self) -> None:
        icon_files = {
            path.name.removesuffix("_line.svg")
            for path in (asset_tool.ASSET_ROOT / "icon" / "svg").glob("*_line.svg")
        }
        illustration_files = {
            path.stem
            for path in (asset_tool.ASSET_ROOT / "illustration" / "png").glob("*.png")
        }
        self.assertEqual(icon_files, set(asset_tool.ICON_KEYWORDS))
        self.assertEqual(illustration_files, set(asset_tool.ILLUSTRATION_KEYWORDS))

    def test_resolve_source_supports_icon_and_illustration_defaults(self) -> None:
        icon_args = types.SimpleNamespace(
            asset_id="icon/tax", format="svg", style="line", size=24
        )
        illustration_args = types.SimpleNamespace(
            asset_id="illustration/m_10_white",
            format="png",
            style="line",
            size=24,
        )
        self.assertTrue(asset_tool.resolve_source(icon_args).is_file())
        self.assertTrue(asset_tool.resolve_source(illustration_args).is_file())


if __name__ == "__main__":
    unittest.main()
