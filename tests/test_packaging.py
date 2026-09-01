import json
import re
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "siit-presentation"
SKILL = PLUGIN / "skills" / "siit-presentation"
ASSETS = SKILL / "assets"


class PackagingTests(unittest.TestCase):
    def test_marketplace_and_plugin_identity(self):
        marketplace = json.loads(
            (ROOT / ".agents" / "plugins" / "marketplace.json").read_text()
        )
        manifest = json.loads(
            (PLUGIN / ".codex-plugin" / "plugin.json").read_text()
        )
        self.assertEqual(marketplace["name"], "siit-presentation")
        self.assertEqual(marketplace["plugins"][0]["name"], "siit-presentation")
        self.assertEqual(manifest["name"], "siit-presentation")
        self.assertEqual(manifest["version"], "0.1.0")

    def test_skill_and_reference_assets_exist(self):
        self.assertIn(
            "name: siit-presentation",
            (SKILL / "SKILL.md").read_text(encoding="utf-8"),
        )
        for path in (
            SKILL / "references" / "workflow.md",
            SKILL / "references" / "style-system.md",
            ASSETS / "siit-reference-template.pptx",
            ASSETS / "siit-noto-sans-kr.thmx",
            ASSETS / "html" / "siit-style-reference.html",
        ):
            self.assertTrue(path.is_file(), path)
        self.assertEqual(len(list((ASSETS / "previews").glob("*.svg"))), 7)

    def test_ooxml_fonts_are_noto_sans_kr(self):
        for path in (
            ASSETS / "siit-reference-template.pptx",
            ASSETS / "siit-noto-sans-kr.thmx",
        ):
            fonts = set()
            with ZipFile(path) as archive:
                for name in archive.namelist():
                    if not name.endswith(".xml"):
                        continue
                    try:
                        root = ET.fromstring(archive.read(name))
                    except ET.ParseError:
                        continue
                    for element in root.iter():
                        if "typeface" in element.attrib:
                            fonts.add(element.attrib["typeface"])
            self.assertEqual(fonts, {"Noto Sans KR"})

    def test_reference_deck_is_sanitized(self):
        path = ASSETS / "siit-reference-template.pptx"
        with ZipFile(path) as archive:
            names = archive.namelist()
            slides = [
                name for name in names
                if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)
            ]
            self.assertEqual(len(slides), 7)
            self.assertFalse(any(
                marker in name for name in names
                for marker in ("notesSlide", "comments", "customXml", "embeddings")
            ))
            payload = b"\n".join(
                archive.read(name) for name in names
                if name.endswith((".xml", ".rels"))
            )
        for private_text in ("고준원", "김준모", "/home/ubuntu"):
            self.assertNotIn(private_text.encode("utf-8"), payload)

    def test_html_reference_is_self_contained(self):
        text = (ASSETS / "html" / "siit-style-reference.html").read_text(
            encoding="utf-8"
        )
        self.assertIn('"Noto Sans KR"', text)
        self.assertNotIn("https://", text)
        self.assertNotIn("http://", text)


if __name__ == "__main__":
    unittest.main()
