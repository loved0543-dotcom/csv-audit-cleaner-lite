from pathlib import Path
import unittest

import yaml


ROOT = Path(__file__).resolve().parent
FORM = ROOT / ".github" / "ISSUE_TEMPLATE" / "lite-feedback.yml"


class FeedbackFormContractTests(unittest.TestCase):
    def test_feedback_form_contract(self):
        data = yaml.safe_load(FORM.read_text(encoding="utf-8"))
        self.assertEqual(data["name"], "CSV Audit Cleaner Lite feedback")
        self.assertEqual(data["title"], "[Lite feedback] ")

        ids = {item.get("id") for item in data["body"] if item.get("id")}
        self.assertTrue(
            {"outcome", "version", "observation", "counts", "privacy"} <= ids
        )

        privacy = next(
            item for item in data["body"] if item.get("id") == "privacy"
        )
        self.assertEqual(privacy["type"], "checkboxes")
        self.assertIs(privacy["attributes"]["options"][0]["required"], True)
        label = privacy["attributes"]["options"][0]["label"]
        for forbidden in (
            "CSV files",
            "customer data",
            "email addresses",
            "local paths",
        ):
            self.assertIn(forbidden, label)

    def test_feedback_link_is_discoverable_without_changing_artifact(self):
        feedback_url = (
            "https://github.com/loved0543-dotcom/csv-audit-cleaner-lite/"
            "issues/new?template=lite-feedback.yml"
        )
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        release = (ROOT / "docs" / "release-notes-v1.0.0.md").read_text(
            encoding="utf-8"
        )

        self.assertEqual(readme.count(feedback_url), 1)
        self.assertEqual(release.count(feedback_url), 1)
        for text in (readme, release):
            self.assertIn("11,174,017 bytes", text)
            self.assertIn(
                "454E5027D3423A792E47B7297AC07C5371D7AAE4486008F3A964A71BEB1D39B1",
                text,
            )


if __name__ == "__main__":
    unittest.main()
