import unittest

from translator import english_to_french, french_to_english

class Testenglish_to_french(unittest.TestCase): 
    def test(self): 
        self.assertNotEqual(english_to_french("hello"), "good night") # test when null is given as input the output is null 
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # test hen 'Hello' is given as input the output is 'Bonjour'
        

class Testfrench_to_english(unittest.TestCase): 
    def test(self): 
        self.assertNotEqual(french_to_english("take"), "bounjour") # test when null is given as input the output is null 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when 'Bonjour' is given as input the output is 'Hello'
    
unittest.main()