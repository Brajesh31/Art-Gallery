"""Unit tests for the static repository validator."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_repository import is_external_reference, markdown_links, resolve_local_reference


class ReferenceValidationTests(unittest.TestCase):
    def test_external_http_reference(self):
        self.assertTrue(is_external_reference("https://example.com/image.png"))

    def test_protocol_relative_reference(self):
        self.assertTrue(is_external_reference("//cdn.example.com/file.css"))

    def test_anchor_is_not_a_filesystem_reference(self):
        self.assertTrue(is_external_reference("#section"))

    def test_relative_reference_resolves(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            target = base / "images" / "picture.jpg"
            target.parent.mkdir()
            target.touch()
            resolved, fragment = resolve_local_reference(base, "images/picture.jpg")
            self.assertEqual(resolved, target.resolve())
            self.assertEqual(fragment, "")

    def test_query_and_fragment_are_parsed(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            target = base / "guide.md"
            target.touch()
            resolved, fragment = resolve_local_reference(base, "guide.md?view=full#setup")
            self.assertEqual(resolved, target.resolve())
            self.assertEqual(fragment, "setup")

    def test_markdown_links_skip_fenced_examples(self):
        fence = chr(96) * 3
        content = f"[real](guide.md)\n\n{fence}text\n[example](not-a-real-file.md)\n{fence}\n"
        self.assertEqual(markdown_links(content), ["guide.md"])

    def test_markdown_images_are_included(self):
        self.assertEqual(markdown_links("![banner](../assets/banner.svg)"), ["../assets/banner.svg"])


if __name__ == "__main__":
    unittest.main()
