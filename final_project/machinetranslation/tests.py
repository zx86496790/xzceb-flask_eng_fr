import unittest
import translator
class TestMyModule(unittest.TestCase):
    def test_e_to_f_1(self):
        self.assertEqual(translator.english_to_french(''),'')
    def test_e_to_f_2(self):
        self.assertEqual(translator.english_to_french('Hello'),'Bonjour')
    def test_f_to_e_1(self):
        self.assertEqual(translator.french_to_english(''),'')
    def test_f_to_e_2(self):
        self.assertEqual(translator.french_to_english('Bonjour'),'Hello')
    if __name__ == '__main__':
        unittest.main()