import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from app import activities


class ActivityCatalogTests(unittest.TestCase):
    def test_github_skills_activity_is_available(self):
        self.assertIn("GitHub Skills", activities)


if __name__ == "__main__":
    unittest.main()
