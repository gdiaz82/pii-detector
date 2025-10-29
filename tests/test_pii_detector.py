from src.regex_detector import RegexPIIDetector
from test_cases import TEST_CASES
import unittest

class TestPIIDetector(unittest.TestCase):
    def setUp(self):
        self.detector = RegexPIIDetector()
    
    def test_all_cases(self):
        """Test que valida tanto tipos como valores específicos"""
        for case in TEST_CASES:
            with self.subTest(case_id=case['id'], text=case['text']):
                results = self.detector.detect(case['text'])
                detected_types = {}
                for result in results:
                    pii_type = result['type']
                    if pii_type not in detected_types:
                        detected_types[pii_type] = []
                    detected_types[pii_type].append(result['value'])
                    
                for expected_type, expected_values in case['expected_pii'].items():
                    self.assertIn(expected_type, detected_types,
                                   f"Case {case['id']}: {expected_type} wasn't detected. Instead {detected_types} was detected.")
                    detected_values = detected_types[expected_type]
                    for expected_value in expected_values:
                        self.assertIn(expected_value, detected_values, f"Case {case['id']}: {expected_value} wasn't detected. Instead {detected_values} was detected.")
                    
                unexpected_types = set(detected_types.keys()) - set(case['expected_pii'].keys())
                if unexpected_types:
                    self.fail(f"Case {case['id']}: Tipos inesperados detectados: {unexpected_types}")
                    
    def test_detailed_detection(self):
        """Test detallado mostrando qué se detectó en cada caso"""
        print("\n" + "="*50)
        print("DETALLES DE DETECCIÓN POR CASO:")
        print("="*50)
        
        for case in TEST_CASES:
            results = self.detector.detect(case['text'])
            
            detected_by_type = {}
            for result in results:
                pii_type = result['type']
                if pii_type not in detected_by_type:
                    detected_by_type[pii_type] = []
                detected_by_type[pii_type].append(result['value'])
            
            print(f"\nCaso {case['id']}:")
            print(f"Texto: '{case['text']}'")
            print(f"Esperado: {case['expected_pii']}")
            print(f"Detectado: {detected_by_type}")

            all_correct = True

            for expected_type, expected_values in case['expected_pii'].items():
                if expected_type not in detected_by_type:
                    print(f"❌ Faltó tipo: {expected_type}")
                    all_correct = False
                else:
                    missing_values = set(expected_values) - set(detected_by_type[expected_type])
                    if missing_values:
                        print(f"❌ Faltó detectar valores: {missing_values}")
                        all_correct = False

            unexpected_types = set(detected_by_type.keys()) - set(case['expected_pii'].keys())
            if unexpected_types:
                print(f"⚠️  Falsos positivos (tipos): {unexpected_types}")
                all_correct = False
            
            if all_correct:
                print("✅ Perfecto!")
    
if __name__ == '__main__':
    unittest.main(verbosity=2)



