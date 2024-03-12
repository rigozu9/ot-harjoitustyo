import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    #saldo setup oikein
    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    #saldo lataus
    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(2500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 35.0)

    #Saldo vähenee oikein, jos rahaa on tarpeeksi
    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 5.0)

    #Saldo ei muutu, jos rahaa ei ole tarpeeksi
    def test_saldo_ei_vahene_jos_ei_rahaa(self):
        self.maksukortti.ota_rahaa(1500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    #Metodi palauttaa True, jos rahat riittivät
    def test_true_jos_rahaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(900), True)

    #Metodi palauttaa False, jos rahat eivät riitä
    def test_true_jos_rahaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1100), False)
        
    
