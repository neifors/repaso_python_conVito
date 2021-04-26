import unittest
import main
from main import data
    
class test_couples(unittest.TestCase):

    def test_n_inscriptions(self):
        self.assertEqual(sum(list(main.n_inscriptions(data))), 51000)
        self.assertEqual(sum(list(main.n_inscriptions(data, "homo"))), 4174)
        self.assertEqual(sum(list(main.n_inscriptions(data, "he"))), 46826)
        self.assertEqual(sum(list(main.n_inscriptions(data, "homosexual f"))), 1445)
        self.assertEqual(sum(list(main.n_inscriptions(data, "homosexual m"))), 2729)

    def test_n_cancelations(self):
        self.assertEqual(sum(list(main.n_cancelations(data))), 9017)
        self.assertEqual(sum(list(main.n_cancelations(data, "homo"))), 916)
        self.assertEqual(sum(list(main.n_cancelations(data, "he"))), 8101)
        self.assertEqual(sum(list(main.n_cancelations(data, "homosexual f"))), 357)
        self.assertEqual(sum(list(main.n_cancelations(data, "homosexual m"))), 559)

    def test_p_inscriptions(self):
        self.assertAlmostEqual(main.p_inscriptions(data, 'he'), 0.918156862)
        self.assertAlmostEqual(main.p_inscriptions(data, 'homo'), 0.08184313725)
        self.assertAlmostEqual(main.p_inscriptions(data, 'homosexual f'), 0.028333333333)
        self.assertAlmostEqual(main.p_inscriptions(data, 'homosexual m'), 0.053509803921)

    def test_p_cancelations(self):
        self.assertAlmostEqual(main.p_cancelations(data, 'he'), 0.898414106687)
        self.assertAlmostEqual(main.p_cancelations(data, 'homo'), 0.101585893312)
        self.assertAlmostEqual(main.p_cancelations(data, 'homosexual f'), 0.03959188200)
        self.assertAlmostEqual(main.p_cancelations(data, 'homosexual m'), 0.061994011)
        
##? PUEDO COMPROBAR RESULTADOS RETURN NUMBER Y EL SUMATORIO DE YIELD QUE VIENE 
##? A SER UN NUMBER TAMBIEN. ¿QUÉ PASA SI EL RESULTADO ES UNA LISTA COMO EN MI CASO
##? LO SON EN annual_p_inscriptions Y annual_p_cancelatiosn?

##? IGUALMENTE, ¿QUÉ PASARÍA SI EL RESULTADO ES UN OBJETO X, O UN DICT?
##? ¿CREAMOS UN CASO DE PRUEBA PARA EL TEST CON UN RESULTADO DE PRUEBA?
        
if __name__ == '__main__':
    unittest.main()