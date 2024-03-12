import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    
    #luo kassan oikein
    def test_luotu_kassa_on_olemassa(self):
        self.assertNotEqual(self.kassa, None)

    #rahamäärä ja myytyjen lounaiden määrä on oikea
    def test_raha_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000)

    #myydyt oikein
    def test_myydyt_oikein(self):
        self.assertEqual((self.kassa.edulliset, self.kassa.maukkaat), (0, 0))

    #Käteisosto toimii sekä edullisten että maukkaiden lounaiden osalta
    
    #Jos maksu riittävä
    def test_edullinen_maksu_riittava(self):
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(340)
        self.assertEqual((self.kassa.kassassa_rahaa_euroina(), vaihtoraha), (1002.4, 100))

    def test_maukas_maksu_riittava(self):
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual((self.kassa.kassassa_rahaa_euroina(), vaihtoraha), (1004, 0))

    def test_lounaat_nousee(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual((self.kassa.edulliset, self.kassa.maukkaat), (1, 1))

    #Jos maksu ei riittävä
    def test_edullinen_maksu_ei_riittava(self):
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(230)
        self.assertEqual((self.kassa.kassassa_rahaa_euroina(), vaihtoraha), (1000, 230))

    def test_maukas_maksu_ei_riittava(self):
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(390)
        self.assertEqual((self.kassa.kassassa_rahaa_euroina(), vaihtoraha), (1000, 390))

    def test_lounaat_eivat_nousee(self):
        self.kassa.syo_edullisesti_kateisella(230)
        self.kassa.syo_maukkaasti_kateisella(390)
        self.assertEqual((self.kassa.edulliset, self.kassa.maukkaat), (0, 0))

    #Korttiosto toimii sekä edullisten että maukkaiden lounaiden osalta
    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    #Jos kortilla on tarpeeksi rahaa
    def test_kortilla_rahat_veloitetaan(self):
        oikein_edullinen = self.kassa.syo_edullisesti_kortilla(self.maksukortti)
        oikein_maukas = self.kassa.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual((oikein_edullinen, oikein_maukas, self.maksukortti.saldo_euroina()), (True, True, 3.60))

    def test_kortilla_lounaat_nousee(self):
        self.kassa.syo_edullisesti_kortilla(self.maksukortti)
        self.kassa.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual((self.kassa.edulliset, self.kassa.maukkaat), (1, 1))

    #Jos kortilla ei tarpeeksi rahaa
    def test_kortilla_rahat__ei_velioteta(self):
        self.kortti = Maksukortti(1)
        oikein_edullinen = self.kassa.syo_edullisesti_kortilla(self.kortti)
        oikein_maukas = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual((oikein_edullinen, oikein_maukas, self.kortti.saldo_euroina()), (False, False, 0.01))

    def test_kortilla_lounaat_eivät_nousee(self):
        self.kortti = Maksukortti(1)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual((self.kassa.edulliset, self.kassa.maukkaat), (0, 0))

    #Kortille rahaa ladattaessa kortin saldo muuttuu ja kassassa oleva rahamäärä kasvaa ladatulla summalla
    def test_kortin_saldo_oikein(self):
        self.kassa.lataa_rahaa_kortille(self.maksukortti, 200)
        self.assertEqual((self.kassa.kassassa_rahaa_euroina(), self.maksukortti.saldo_euroina()), (1002.0, 12.0))

    #Kortille rahaa ladattaessa kortin saldo ei muutu jos negatiivinen summa
    def test_kortin_saldo_oikein_jos_summa_nega(self):
        self.kassa.lataa_rahaa_kortille(self.maksukortti, -200)
        self.assertEqual((self.kassa.kassassa_rahaa_euroina(), self.maksukortti.saldo_euroina()), (1000.0, 10.0))