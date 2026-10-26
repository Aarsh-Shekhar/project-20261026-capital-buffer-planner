import unittest

from capital_buffer_planner.models import Record
from capital_buffer_planner.scoring import score_record


class DepthCheck5(unittest.TestCase):
    def test_005_backlog_triage(self):
        record = Record(id="scenario-005", exposure=80263, signal=0.256, urgency=3)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
