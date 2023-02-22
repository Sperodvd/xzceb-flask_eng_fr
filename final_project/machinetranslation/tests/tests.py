import unittest
import translator

class TestFr2EnMethod(unittest.TestCase):
    def test_translateBonjour(self):
        frenchText = 'Bonjour'
        translatedText = translator.french_to_english(frenchText)
        self.assertEquals(translatedText, "Hello")
    def test_translateNull(self):
        frenchText = ''
        with self.assertRaises(Exception):
            translator.french_to_english(frenchText)

class TestEn2FrMethod(unittest.TestCase):
    def test_translateHello(self):
        englishText = 'Hello'
        translatedText = translator.english_to_french(englishText)
        self.assertEquals(translatedText, "Bonjour")
    def test_translateNull(self):
        englishText = ''
        with self.assertRaises(Exception):
            translator.french_to_english(englishText)

if __name__=='__main__':
    unittest.main()