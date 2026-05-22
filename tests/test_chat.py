import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
BACKEND_DIR = PROJECT_ROOT / "backend"
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from agent_service import classify_request


class ClassifyRequestTests(unittest.TestCase):
    def test_weather_routes_to_search_not_time(self):
        self.assertEqual(
            classify_request("What's the weather in Los Angeles today?"),
            "search",
        )

    def test_thursday_game_routes_to_search_not_time(self):
        self.assertEqual(
            classify_request("Who won the Knicks/cavs game Thursday?"),
            "search",
        )

    def test_day_question_routes_to_time(self):
        self.assertEqual(
            classify_request("What day is it today?"),
            "time",
        )

    def test_plain_time_question_routes_to_time(self):
        self.assertEqual(
            classify_request("What time is it right now?"),
            "time",
        )

    def test_conversion_question_routes_to_conversion(self):
        self.assertEqual(
            classify_request("Convert 10 miles to kilometers"),
            "conversion",
        )

    def test_math_question_routes_to_math(self):
        self.assertEqual(
            classify_request("Calculate 13 + 7"),
            "math",
        )


if __name__ == "__main__":
    unittest.main()
