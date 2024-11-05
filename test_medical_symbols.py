import unittest
from medical_symbols import MedicalSymbolExtractor

class TestMedicalSymbolExtractor(unittest.TestCase):
    def setUp(self):
        self.extractor = MedicalSymbolExtractor()
        
    def test_symbol_extraction(self):
        test_text = "BP ↑ 140/90 mmHg"
        result = self.extractor.extract_symbols(test_text)
        self.assertTrue(any(s['symbol'] == '↑' for s in result['symbols']))
        self.assertTrue(any(u['unit'] == 'mmHg' for u in result['units']))
        
    def test_numeric_context(self):
        test_text = "Temperature: 38.5°"
        result = self.extractor.extract_symbols(test_text)
        self.assertTrue('38.5°' in result['contexts'])
        
    def test_empty_text(self):
        test_text = ""
        result = self.extractor.analyze_text(test_text)
        self.assertEqual(result['total_symbols'], 0)
        self.assertEqual(result['total_units'], 0)
        
    def test_multiple_symbols(self):
        test_text = "↑BP ↓HR ±2mg/dL"
        result = self.extractor.analyze_text(test_text)
        self.assertEqual(result['total_symbols'], 3)

if __name__ == '__main__':
    unittest.main()
