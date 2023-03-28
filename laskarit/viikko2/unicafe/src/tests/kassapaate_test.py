import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)


    def test_kassa_olemassa(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)
    
    def test_syo_edullisesti_kateisella(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(300),60)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        self.assertEqual(self.kassa.edulliset, 1)


    def test_syo_maukkaasti_kateisella(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(450), 50)
        self.assertEqual(self.kassa.kassassa_rahaa,100400)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_raha_ei_riita(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(230),230)
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(390),390)
        self.assertEqual(self.kassa.edulliset,0)
        self.assertEqual(self.kassa.maukkaat,0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_korttimaksut_raha_riittaa(self):
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti),True)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.60 euroa")
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), True)
        self.assertEqual(str(self.kortti),"Kortilla on rahaa 3.60 euroa")
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_korttimaksut_raha_ei_riita(self):
        kortti = Maksukortti(230)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(kortti), False)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.30 euroa")
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(kortti), False)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.30 euroa")
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kortille_rahan_lataus(self):
        self.assertEqual(self.kassa.lataa_rahaa_kortille(self.kortti, 100), None)
        self.assertEqual(self.kassa.kassassa_rahaa, 100100)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 11.00 euroa")

    def test_kortille_rahan_lataus_neg(self):
        self.assertEqual(self.kassa.lataa_rahaa_kortille(self.kortti, -100), None)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")