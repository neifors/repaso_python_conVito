import unittest
import main
from main import data
    
class test_deas(unittest.TestCase):

    def test_n_deas(self):
        self.assertEqual(main.n_deas(data), 7640)
        
        
if __name__ == '__main__':
    unittest.main()