import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_saldo_lataus(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")

    def test_rahan_kaytto(self):
        self.maksukortti.ota_rahaa(250)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.50 euroa")
    
    def test_raha_ei_riita(self):
        kortti = Maksukortti(200)
        self.maksukortti.ota_rahaa(250)
        self.assertEqual(str(kortti),"Kortilla on rahaa 2.00 euroa")
    
    def test_raha_nosto_riittava(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1000), True)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 0.00 euroa")

    def test_raha_nosto_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1100), False)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")