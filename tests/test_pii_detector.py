from src.regex_detector import RegexPIIDetector
from test_cases import TEST_CASES
import unittest

class TestPIIDetector(unittest.TestCase):
    def setUp(self):
        self.detector = RegexPIIDetector()
    
    def test_all_cases(self):
        for case in TEST_CASES:
            with self.subTest(case_id=case['id'], text=case['text']):
                results = self.detector.detect(case['text'])
                detected_types = [result['type'] for result in results]
                for expected_type in case['expected_pii']:
                    self.assertIn(expected_type, detected_types,
                                   f"Case {case['id']}: {expected_type} wasn't detected. Instead {detected_types} was detected.")
                    
                if not case['expected_pii']:
                    self.assertEqual(len(detected_types), 0,
                                     f"Case {case['id']}: {detected_types} false positives.")
    
if __name__ == '__main__':
    unittest.main(verbosity=2)



