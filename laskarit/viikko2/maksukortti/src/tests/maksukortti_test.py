import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    #setup card with 10€
    def setUp(self):
        self.kortti = Maksukortti(1000)

    #saldo setup oikein
    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")

    #syö edullisesti
    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()

        self.assertEqual(self.kortti.saldo_euroina(), 7.5)

    #syö edullisesti ei vie negatiiviseksi saldoa
    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        kortti.syo_edullisesti()

        self.assertEqual(kortti.saldo_euroina(), 2.0)

    #syö maukkaasti 
    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_maukkaasti()

        self.assertEqual(self.kortti.saldo_euroina(), 6.0)

    #syö maukkaasti ei vie negatiiviseksi saldoa
    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(300)
        kortti.syo_maukkaasti()

        self.assertEqual(kortti.saldo_euroina(), 3.0)

    #saldo lataus
    def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(2500)

        self.assertEqual(self.kortti.saldo_euroina(), 35.0)

    #negative money test
    def test_kortille_ei_voi_ladata_negatiivista_rahaa(self):
        self.kortti.lataa_rahaa(-2500)
        self.assertEqual(self.kortti.saldo_euroina(), 10.0)

    #ei voi lataa enempään kuin maksimiarvoa
    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
        self.kortti.lataa_rahaa(20000)

        self.assertEqual(self.kortti.saldo_euroina(), 150.0)

    #edulisen lounaan osto kun 2.5€ kortilla
    def test_voi_ostaa_edullisen_kun_250(self):
        kortti = Maksukortti(250)
        kortti.syo_edullisesti()

        self.assertEqual(kortti.saldo_euroina(), 0.0)

    #maukkaan lounaan osto kun 4.0€ kortilla
    def test_voi_ostaa_edullisen_kun_250(self):
        kortti = Maksukortti(400)
        kortti.syo_maukkaasti()

        self.assertEqual(kortti.saldo_euroina(), 0.0)
    