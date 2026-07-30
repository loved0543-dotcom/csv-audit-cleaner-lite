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

    def test_v101_release_contract_and_feedback_link_are_discoverable(self):
        feedback_url = (
            "https://github.com/loved0543-dotcom/csv-audit-cleaner-lite/"
            "issues/new?template=lite-feedback.yml"
        )
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        release = (ROOT / "docs" / "release-notes-v1.0.1.md").read_text(
            encoding="utf-8"
        )
        form = FORM.read_text(encoding="utf-8")

        self.assertEqual(readme.count(feedback_url), 1)
        self.assertEqual(release.count(feedback_url), 1)
        for text in (readme, release):
            self.assertIn("CSV_Audit_Cleaner_Lite_v1.0.1.zip", text)
            self.assertIn("11,174,177 bytes", text)
            self.assertIn(
                "7787166796EDFB71C892CCDB2DE0A437FA046E9D2C9A66B2EE831AD427D6B21C",
                text,
            )
        self.assertIn("value: v1.0.1", form)


if __name__ == "__main__":
    unittest.main()
