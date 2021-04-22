import unittest
import main as subject

my_path = Path('./analisis parejas/data')

with open(my_path / 'parejas.json', 'r', encoding="utf8") as file:
    data = json.load(file)
    
class test_couples(unittest.TestCase):

    def test_n_of_sample(self):
        self.assertEqual(subject.n_,)

if __name__ == '__main__':
    unittest.main()