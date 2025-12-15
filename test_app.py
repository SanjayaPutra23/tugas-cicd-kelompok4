import unittest
from app import tambah, kurang

class TestKalkulator(unittest.TestCase):

    def test_tambah(self):
        self.assertEqual(tambah(3, 4), 7)
        self.assertEqual(tambah(-1, 1), 0)
        print("LOG: Test Penjumlahan Berhasil.")

    def test_kurang(self):
        self.assertEqual(kurang(10, 5), 5)
        self.assertEqual(kurang(5, 10), -5)
        print("LOG: Test Pengurangan Berhasil.")

if __name__ == '__main__':
    unittest.main()