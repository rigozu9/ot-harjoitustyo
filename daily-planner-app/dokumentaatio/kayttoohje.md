# Käyttöohje

Tarvitset projektin toimimiseen pythonin, poetryn ja psql:n.
Lataa projektin loppupalautus [release](https://github.com/rigozu9/ot-harjoitustyo/releases)

## Ohjelman suorittaminen
Navigoi daily-planner-app folderiin ja asenna riippuvuudet komennolla:

```bash
poetry install
```

Mene poetryn virtual enviin komennolla: 

```bash
poetry shell
```

Ja suorita ohjelma komennolla:

```bash
poetry run invoke start
```

### Sovelluksessa
Tämän jälkeen voit rekiseröityöä sovellukseen.

Rekisteröitymisen jälkeen kirjaudut sisään ja ensikirjautumisella vastaat kyselyyn.

Kyselyssä päätät tavoitteitasi.

Kyselyn jälkeen päädyt päivän suunnitelma näkymään, jossa voit kertoa mitä teit sinä päivänä.

Kun olet laittanut tunnit ja muut siihen saat yhteenvedon päivästäsi ja vertailut tavoitteihin.
Voit myös poitaa päivän pläänin ja tehdä sen uudelleen.

Siitä voit navigoida omaan profiiliisi tai kalenteriin.

Omassa profiilissa näät tavoitteesi ja keskiverto aktiviteetit, myös vertaukset tavoitteisiin.
Pääset täältä myös vinkkinäkymään, jossa on sinulle räätälöityjä vinkkejä ja linkkejä hyödyllisille sivustoille.
Myös lähteet mitä käytettiin vinkeissä löytyy täältä.

Kalenterissa voit lisätä muille päiville aktiviteetit.

Sovelluksen voi sulkea raksia painamalla, tiedot ovat tallentuneet tietokantaan.

## Invoke komennot:
### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint tarkistus

Pylintin tarkistus komento:

```bash
poetry run invoke lint
```