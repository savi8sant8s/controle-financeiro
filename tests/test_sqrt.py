import unittest
import math

class TestarRaizQuadrada(unittest.TestCase):

    def testar_raiz_64(self):
        self.assertEqual(8, math.sqrt(64))

if __name__ == '__main__':
    unittest.main()